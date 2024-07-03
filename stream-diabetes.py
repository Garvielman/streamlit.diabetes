import pickle
import streamlit as st

# Load model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

st.title('Prediction Diabetes')

# Input data
col1, col2 = st.columns(2)

with col1:
    Age = st.number_input('Input Umur', min_value=0, max_value=120, step=1)

with col2:
    Gender = st.selectbox('Input Gender', ['Male', 'Female'])

with col1:
    Polyuria = st.selectbox('Input Polyuria', ['Yes', 'No'])

with col2:
    Polydipsia = st.selectbox('Input Polydipsia', ['Yes', 'No'])

with col1:
    Suddenweightloss = st.selectbox('Input Sudden Weight Loss', ['Yes', 'No'])

with col2:
    Weakness = st.selectbox('Input Weakness', ['Yes', 'No'])

with col1:
    Polyphagia = st.selectbox('Input Polyphagia', ['Yes', 'No'])

with col2:
    Genitalthrush = st.selectbox('Input Genital Thrush', ['Yes', 'No'])

with col1:
    Visualblurring = st.selectbox('Input Visual Blurring', ['Yes', 'No'])

with col2:
    Itching = st.selectbox('Input Itching', ['Yes', 'No'])

with col1:
    Irritability = st.selectbox('Input Irritability', ['Yes', 'No'])

with col2:
    Delayedhealing = st.selectbox('Input Delayed Healing', ['Yes', 'No'])

with col1:
    Partialparesis = st.selectbox('Input Partial Paresis', ['Yes', 'No'])

with col2:
    Musclestiffness = st.selectbox('Input Muscle Stiffness', ['Yes', 'No'])

with col1:
    Alopecia = st.selectbox('Input Alopecia', ['Yes', 'No'])

with col2:
    Obesity = st.selectbox('Input Obesity', ['Yes', 'No'])

# Convert input to numerical values
Gender = 1 if Gender == 'Male' else 0
Polyuria = 1 if Polyuria == 'Yes' else 0
Polydipsia = 1 if Polydipsia == 'Yes' else 0
Suddenweightloss = 1 if Suddenweightloss == 'Yes' else 0
Weakness = 1 if Weakness == 'Yes' else 0
Polyphagia = 1 if Polyphagia == 'Yes' else 0
Genitalthrush = 1 if Genitalthrush == 'Yes' else 0
Visualblurring = 1 if Visualblurring == 'Yes' else 0
Itching = 1 if Itching == 'Yes' else 0
Irritability = 1 if Irritability == 'Yes' else 0
Delayedhealing = 1 if Delayedhealing == 'Yes' else 0
Partialparesis = 1 if Partialparesis == 'Yes' else 0
Musclestiffness = 1 if Musclestiffness == 'Yes' else 0
Alopecia = 1 if Alopecia == 'Yes' else 0
Obesity = 1 if Obesity == 'Yes' else 0

diab_diagnosis = ''

if st.button('Test Prediction Diabetes'):
    input_data = [Age, Gender, Polyuria, Polydipsia, Suddenweightloss, Weakness, Polyphagia, Genitalthrush, Visualblurring, Itching, Irritability, Delayedhealing, Partialparesis, Musclestiffness, Alopecia, Obesity]
    
    # Display input data for debugging
    st.write("Input data:", input_data)
    
    # Reshape the input data to match the model's expected input format
    diab_prediction = diabetes_model.predict([input_data])

    if diab_prediction[0] == 1:
        diab_diagnosis = 'Pasien terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena Diabetes'

    st.success(diab_diagnosis)
