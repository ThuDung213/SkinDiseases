import streamlit as st
import tensorflow as tf
import numpy as np
import mysql.connector


def connect_to_db():
    return mysql.connector.connect(
        host="localhost",  
        user="root",       
        password="",       
        database="skin" 
    )

def get_disease_info(disease_name):
    conn = connect_to_db()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT details, treatment FROM diseases WHERE name = %s"
    cursor.execute(query, (disease_name,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

# Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_skin_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(
        test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)  # return index of max element


# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox(
    "Select Page", ["Home", "About", "Disease Recognition"])

# Main Page
if (app_mode == "Home"):
    st.header("SKIN DISEASE RECOGNITION SYSTEM")
    image_path = "skin-image.jpg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
    Welcome to the Skin Disease Detection System! 🌟🔍

    Our mission is to help in identifying skin diseases efficiently. Upload an image of the affected skin area, and our system will analyze it to detect any signs of diseases. Together, let's ensure healthier skin and better health!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of the skin area with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Skin Disease Detection System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

# About Project
elif (app_mode == "About"):
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github repo.
                This dataset consists of about 87K rgb images of healthy and diseased crop leaves which is categorized into 38 different classes.The total dataset is divided into 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing 1735 test images is created later for prediction purpose.
                #### Content
                1. train (13892 images)
                2. test (1735 images)
                3. validation (1735 images)

                """)

# Prediction Page
elif (app_mode == "Disease Recognition"):
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if test_image:
        if (st.button("Show Image")):
            st.image(test_image, width=4, use_column_width=True)
        
        # Predict 
        if 'predict_button' not in st.session_state:
            st.session_state["predict_button"] = False
        if 'details_button' not in st.session_state:
            st.session_state["details_button"] = False
        if 'result_index' not in st.session_state:
            st.session_state.result_index = None

        if st.button("Predict"):
            st.session_state["predict_button"] = not st.session_state["predict_button"]
            
            
        if st.session_state["predict_button"]:
            st.snow()
            st.write("Our Prediction")
            st.session_state.result_index = model_prediction(test_image)
            # Reading Labels
            class_name = ['Eczema 1677', 'Melanoma', 'Atopic Dermatitis',
                        'Basal Cell Carcinoma (BCC)', 'Melanocytic Nevi (NV)']
            st.success("Model is Predicting it's a {}".format(
                class_name[st.session_state.result_index]))
            
            if (st.button("See Detailed Information of Disease")):
                st.session_state["details_button"] = not st.session_state["details_button"]

        if st.session_state["details_button"]:
            disease_info = get_disease_info(class_name[st.session_state.result_index])
            st.write("### Basic Information from Database")
            st.write(f"**Details:** {disease_info['details']}")
            st.write(f"**Treatment:**")
            st.markdown(disease_info['treatment'].replace('\n', '<br>'), unsafe_allow_html=True)
