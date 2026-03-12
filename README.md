# 🐾 Animal Crossing Detection Using CSI Data

## 📌 Project Overview
This project detects animal movement on rural roads using simulated WiFi Channel State Information (CSI) data.

The system classifies movement into:
- Small Animal
- Medium Animal
- Large Animal

It works in simulated real-time and generates alerts when an animal is detected.

---

## 🧠 Technologies Used
- Python
- NumPy
- Scikit-learn
- TensorFlow (LSTM)
- Flask (Backend API)
- Streamlit (Dashboard)

---

## 🚀 How To Run

1. Install dependencies:
   pip install -r requirements.txt

2. Generate dataset:
   python data/generate_data.py

3. Train model:
   python models/train_rf.py

4. Start backend:
   python backend/app.py

5. Run dashboard:
   streamlit run dashboard/streamlit_app.py

---

## 📊 Features
- Signal Processing (FFT, Filtering)
- Random Forest Model
- LSTM Model
- Flask API
- Streamlit Dashboard
- Alert System