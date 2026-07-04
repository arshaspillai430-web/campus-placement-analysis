import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("placement_model.pkl")

st.title("Placement Prediction System")

st.write("Enter student details:")

# Inputs (MUST match training features)
ssc_p = st.number_input("SSC Percentage")
hsc_p = st.number_input("HSC Percentage")
degree_p = st.number_input("Degree Percentage")
etest_p = st.number_input("E-Test Percentage")
mba_p = st.number_input("MBA Percentage")
workex = st.selectbox("Work Experience (0 = No, 1 = Yes)", [0, 1])

# Prediction
if st.button("Predict"):
    features = np.array([[ssc_p, hsc_p, degree_p, etest_p, mba_p, workex]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Student is LIKELY to be PLACED 🎉")
    else:
        st.error("Student is NOT likely to be placed ❌")