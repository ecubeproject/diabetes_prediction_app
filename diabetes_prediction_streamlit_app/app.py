import streamlit as st
import pandas as pd
import pickle
# Load the serialized model
with open('diabetes_model.pkl', 'rb') as file:
    model = pickle.load(file)
# Streamlit webpage configuration
st.title('Diabetes Prediction App')
st.write('This application predicts whether a patient is likely to have diabetes based on diagnostic measures.')
# Collecting user input features into dataframe
def user_input_features():
    NumPregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1)
    Glucose = st.number_input('Glucose Level', min_value=0, max_value=200, step=1) 
    BloodPressure = st.number_input('Blood Pressure', min_value=0, max_value=122, step=1)
    SkinThickness = st.number_input('Skin Thickness', min_value=0, max_value=99, step=1)
    Insulin = st.number_input('Insulin Level', min_value=0, max_value=846, step=1)
    BMI = st.slider('BMI', min_value=0.0, max_value=70.0)
    DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function', min_value=0.0, max_value=2.5)
    Age= st.number_input('Age', min_value=21, max_value=100, step=1)
    data = {
    'NumPregnancies':NumPregnancies,
    'Glucose': Glucose,
    'BloodPressure': BloodPressure,
    'SkinThickness': SkinThickness,
    'Insulin': Insulin,
    'BMI': BMI,
    'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
    'Age': Age
    }
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_features()

if st.button('Predict'):
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[0][1]
    st.write(f'Prediction: {"Diabetic" if prediction[0] == 1 else "Not Diabetic"}')
    st.write(f'Probability of being diabetic: {probability:.2f}')