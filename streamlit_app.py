# # Importing Important Libraries
import pickle
import streamlit as st
import numpy as np

# Load model
model_diabetes = pickle.load(open('model_diabetes_logistic.sav', 'rb'))

# Web Title
st.title('Diabetes Prediction')

# Dictionary to store input labels and user input values
input_fields = {
    'Pregnancies': 'Enter the Pregnancies value',
    'Glucose': 'Enter the Glucose value',
    'BloodPressure': 'Enter the Blood Pressure value',
    'SkinThickness': 'Enter the Skin Thickness value',
    'Insulin': 'Enter the Insulin value',
    'BMI': 'Enter the BMI value',
    'DiabetesPedigreeFunction': 'Enter the Diabetes Pedigree Function value',
    'Age': 'Enter the Age value'
}

# Create dynamic input fields in columns
user_inputs = {}
col1, col2 = st.columns(2)
with col1:
    for field, label in list(input_fields.items())[:4]:  # First 4 fields in col1
        user_inputs[field] = st.number_input(label)
        
with col2:
    for field, label in list(input_fields.items())[4:]:  # Remaining fields in col2
        user_inputs[field] = st.number_input(label)

# Prediction button
diabetes_diagnosis = ''

if st.button('Diabetes Prediction Test'):
    # Prepare the input data for prediction
    input_data = [list(user_inputs.values())]

    # Make prediction
    diabetes_prediction = model_diabetes.predict(input_data)
    
    if diabetes_prediction[0] == 1:
        diabetes_diagnosis = 'The patient has diabetes'
    else:
        diabetes_diagnosis = 'The patient does not have diabetes'

# Show result
st.success(diabetes_diagnosis)
