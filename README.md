# 🐾 Animal Crossing Detection System using CSI Signals

A real-time AI-based monitoring system that detects animal crossings using simulated Channel State Information (CSI) signals. The system analyzes signal distortion patterns and classifies animal movement using machine learning.

---

## 📌 Project Overview

Road accidents caused by unexpected animal crossings are a major safety concern. Traditional camera-based systems fail in low-light or adverse weather conditions.

This project provides a **signal-based detection system** that works using wireless signal distortion (CSI), making it more robust and reliable.

---

## ⚙️ Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Random Forest (Scikit-learn)
* **Signal Processing:** NumPy
* **Frontend:** HTML, CSS, JavaScript
* **Visualization:** Chart.js

---

## 🚀 Features

✔ Real-time animal detection
✔ Live CSI signal visualization
✔ Detection confidence (%)
✔ Smart alert system (with cooldown + sound)
✔ Detection history with timestamps
✔ Statistics dashboard (chart-based)
✔ Admin panel (all-in-one monitoring)
✔ CSV report export
✔ Responsive UI dashboard

---

## 🧠 How It Works

```text
CSI Signal (Simulated)
        ↓
Signal Preprocessing
        ↓
Feature Extraction
        ↓
Machine Learning Model
        ↓
Prediction (Animal Type)
        ↓
Dashboard + Alerts + Stats
```

---

## 📊 Detection Categories

* No Animal Detected
* Small Animal
* Medium Animal
* Large Animal

---

## 🖥️ Screenshots

> Add screenshots here for better presentation

* Dashboard
* Stats Page
* Admin Panel
* History Page

---

## 📂 Project Structure

```bash
animal-csi-detection/
│
├── backend/
│   └── app.py
│
├── utils/
│   ├── preprocessing.py
│   ├── feature_extraction.py
│   ├── history.py
│   └── stats.py
│
├── ml/
│   ├── train_model.py
│   └── predict.py
│
├── templates/
│   ├── dashboard.html
│   ├── stats.html
│   ├── history.html
│   └── admin.html
│
├── static/
│   ├── style.css
│   └── alert.mp3
│
└── README.md
```

---

## 🛠️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/animal-csi-detection.git

# Navigate to project folder
cd animal-csi-detection

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m backend.app
```

---

## 🌐 Access the System

Open in browser:

```text
http://127.0.0.1:5000/
```

---

## 📊 Available Pages

| Page        | URL      |
| ----------- | -------- |
| Dashboard   | /        |
| Stats       | /stats   |
| History     | /history |
| Admin Panel | /admin   |

---

## 📥 Export Feature

Download detection logs as CSV:

```text
/admin → Download Report
```

---

## 🎯 Key Highlights

* Real-time monitoring system
* AI-based prediction with confidence
* Smart alert mechanism (no spam alerts)
* Data logging and analytics dashboard

---

## 🔮 Future Scope

* Integration with real CSI hardware (ESP32 / Intel 5300)
* Mobile notification system
* IoT-based deployment on highways
* Deep learning-based classification

---

## 👥 Team Contribution

* **Ravi Raj** → Backend, ML, Dashboard, System Integration
* **Partner Name** → History, Stats, UI Enhancements, Logging System

---

## 🎤 Viva Explanation (Short)

> This system detects animal crossings by analyzing wireless signal distortions. It processes the signal, extracts features, and uses a machine learning model to classify the type of animal. The system provides real-time alerts, confidence levels, and analytics through a dashboard.

---

## 🏆 Final Output

```text
AI Monitoring Dashboard + Alerts + Analytics + Report System
```

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

---


## Authors

Ravi Kumar

Rinku

Sonu Bhai Patel

B.Tech Software Engineering Project
