import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("models/model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️")

st.title("❤️ Heart Disease Prediction System")

st.write(
    "Enter the patient's details below to predict whether they are likely to have heart disease."
)

# Input fields
age = st.number_input("Age", 20, 100, 45)

sex = st.selectbox("Sex", ["Female", "Male"])
sex = 1 if sex == "Male" else 0

cp = st.selectbox(
    "Chest Pain Type",
    [0, 1, 2, 3],
    help="0=Typical Angina, 1=Atypical Angina, 2=Non-anginal Pain, 3=Asymptomatic"
)

trestbps = st.number_input("Resting Blood Pressure", 80, 220, 120)

chol = st.number_input("Cholesterol", 100, 600, 200)

fbs = st.selectbox("Fasting Blood Sugar >120 mg/dl", [0, 1])

restecg = st.selectbox("Resting ECG", [0, 1, 2])

thalach = st.number_input("Maximum Heart Rate", 60, 220, 150)

exang = st.selectbox("Exercise Induced Angina", [0, 1])

oldpeak = st.number_input("ST Depression", 0.0, 7.0, 1.0)

slope = st.selectbox("Slope", [0, 1, 2])

ca = st.selectbox("Number of Major Vessels", [0, 1, 2, 3, 4])

thal = st.selectbox("Thal", [0, 1, 2, 3])

# Predict button
if st.button("Predict"):

    features = np.array([[age, sex, cp, trestbps, chol,
                          fbs, restecg, thalach,
                          exang, oldpeak, slope,
                          ca, thal]])

    features = scaler.transform(features)

    prediction = model.predict(features)

    probability = model.predict_proba(features)[0][1]

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

    st.write(f"Prediction Confidence: **{probability:.2%}**")