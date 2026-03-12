import streamlit as st
import numpy as np
import requests
import time

st.title("🐾 Animal Crossing Detection System")

def generate_signal():
    base = np.random.normal(0, 0.2, (200, 30))
    disturbance = np.sin(np.linspace(0, 8, 200)).reshape(-1, 1)
    return base + disturbance

signal = generate_signal()

st.subheader("Live CSI Signal (Subcarrier 1)")
st.line_chart(signal[:, 0])

if st.button("Detect Animal"):
    response = requests.post(
        "http://127.0.0.1:5000/predict",
        json={"signal": signal.tolist()}
    )

    result = response.json()

    st.success(f"Prediction: {result['prediction']}")
    st.info(f"Confidence: {result['confidence']}")

    if result["confidence"] > 0.8:
        st.error("⚠ ALERT! Animal Crossing Detected!")