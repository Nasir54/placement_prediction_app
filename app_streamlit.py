import streamlit as st
import numpy as np
import joblib

# Load trained model and scaler
model = joblib.load("model/model.joblib")
scaler = joblib.load("model/scaler.joblib")

st.title("📊 Placement Prediction App")
st.write("Enter student details to predict placement outcome")

# Input fields
cgpa = st.number_input("Enter CGPA", min_value=0.0, max_value=10.0, step=0.1)
iq = st.number_input("Enter IQ Level", min_value=0, max_value=200, step=1)

# Prediction button
if st.button("Predict"):
    # Scale input
    features = scaler.transform([[cgpa, iq]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("🎉 The student is likely to be placed!")
    else:
        st.error("❌ The student is unlikely to be placed.")
