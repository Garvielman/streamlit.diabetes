import pickle
import streamlit as st

# Load model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

st.title('Prediction Diabetes')

col1, col2 = st.columns(2)

with col1:
    Age = st.text_input('Input Umur')

with col2:
    Gender = st.text_input('Input Gender')

with col1:
    Polyuria = st.text_input('Input Polyuria')

with col2:
    Polydipsia = st.text_input('Input Polydipsia')

with col1:
    Suddenweightloss = st.text_input('Input Sudden Weight Loss')

with col2:
    Weakness = st.text_input('Input Weakness')

with col1:
    Polyphagia = st.text_input('Input Polyphagia')

with col2:
    Genitalthrush = st.text_input('Input Genital Thrush')

with col1:
    Visualblurring = st.text_input('Input Visual Blurring')

with col2:
    Itching = st.text_input('Input Itching')

with col1:
    Irritability = st.text_input('Input Irritability')

with col2:
    Delayedhealing = st.text_input('Input Delayed Healing')

with col1:
    Partialparesis = st.text_input('Input Partial Paresis')

with col2:
    Musclestiffness = st.text_input('Input Muscle Stiffness')

with col1:
    Alopecia = st.text_input('Input Alopecia')

with col2:
    Obesity = st.text_input('Input Obesity')

diab_diagnosis = ''

if st.button('Test Prediction Diabetes'):
    try:
        # Convert inputs to appropriate data types
        input_data = [int(Age), int(Gender), int(Polyuria), int(Polydipsia), int(Suddenweightloss),
                      int(Weakness), int(Polyphagia), int(Genitalthrush), int(Visualblurring),
                      int(Itching), int(Irritability), int(Delayedhealing), int(Partialparesis),
                      int(Musclestiffness), int(Alopecia), int(Obesity)]
        
        # Reshape the input data to match the model's expected input format
        diab_prediction = diabetes_model.predict([input_data])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'Pasien terkena Diabetes'
        else:
            diab_diagnosis = 'Pasien tidak terkena Diabetes'

        st.success(diab_diagnosis)
    except ValueError:
        st.error('Please ensure all inputs are valid integers.')
