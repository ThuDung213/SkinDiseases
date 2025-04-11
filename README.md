# Skin Diseases Detection System

## Overview
The Skin Diseases Detection System is a machine learning-based web application designed to assist in the detection and recognition of skin diseases from uploaded images. The system classify skin diseases into various categories and provides detailed information and treatment recommendations for the detected disease.

## Dataset
https://drive.google.com/drive/folders/13lJzRvIOMAu5GvFyGz5xlwDsj8la1ki_?usp=drive_link

## Features
1. Disease Recognition: Upload an image of a skin condition, and the system will predict the disease category.
2. Detailed Information: Provides information about the disease and possible treatments.

## Project Structure
```
SkinDiseasesWeb/
├── main.py                  # Main application file
├── Train_skin_disease.ipynb # Notebook for training the model
├── Test_skin_disease.ipynb  # Notebook for testing the model
├── trained_skin_disease_model.keras # Pre-trained model
├── requirements.txt         # Python dependencies
├── output/                  # Directory containing test, train, and validation datasets
└── README.md 
```

## Workflow
1. Upload an Image: Users can upload an image of a skin condition through the "Disease Recognition" page.
2. Prediction: The uploaded image is processed by a deep learning model (trained_skin_disease_model.keras) to predict the disease category.
3. Results: The system displays the predicted disease along with detailed information and treatment recommendations retrieved from a MySQL database.