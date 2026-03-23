# Animal Crossing Detection System Using CSI Data

## Overview

This project detects animal crossings on rural roads using simulated Channel State Information (CSI) signals. When an animal moves across a wireless signal path, the signal pattern changes. The system analyzes these changes using signal processing and machine learning to detect possible animal crossings.

The goal of this project is to improve road safety by providing a real-time alert system that warns about animal movement near roads.

---

## Problem Statement

Animal crossings on rural roads often cause accidents and wildlife fatalities. Traditional camera-based systems may fail in poor lighting or bad weather conditions.

This project proposes a non-visual sensing system that uses wireless signal distortions to detect animal movement.

---

## System Architecture

Signal Simulator
↓
Signal Preprocessing
↓
Feature Extraction
↓
Machine Learning Model
↓
Animal Detection
↓
Flask Backend
↓
Real-Time Dashboard

---

## Key Features

* CSI signal simulation
* Signal preprocessing and normalization
* Feature extraction using FFT
* Machine learning based detection
* Real-time signal visualization
* Auto-updating detection dashboard
* Animal alert system with icons
* Model accuracy visualization


---

## Tech Stack

Backend

* Python
* Flask

Machine Learning

* Scikit-learn
* Random Forest

Signal Processing

* NumPy
* FFT

Visualization

* Chart.js
* HTML
* CSS

---

## Project Structure

```
animal-csi-detection
│
├── backend
│   └── app.py
│
├── alerts
│   └── alert_system.py
│
├── config
│   └── settings.py
│
├── data
│   └── generate_data.py
│
├── ml
│   ├── train_model.py
│   └── predict.py
│
├── models
│   └── model.pkl
│
├── utils
│   ├── preprocessing.py
│   ├── feature_extraction.py
│   └── signal_simulator.py
│
├── templates
│   └── dashboard.html
│
├── static
│   └── style.css
│
└── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/your-username/animal-crossing-detection.git
```

Navigate to the project folder

```
cd animal-csi-detection
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Running the Project

Start the Flask server

```
python -m backend.app
```

Open browser

```
http://127.0.0.1:5000
```

---

## Machine Learning Model

The system uses a Random Forest classifier trained on simulated CSI signal features.

Extracted features include:

* Mean
* Standard Deviation
* Maximum Value
* Minimum Value
* Signal Energy

These features help classify animal movement into categories such as:

* No Animal
* Small Animal
* Medium Animal
* Large Animal

---

## Expected Outcomes

* Improved road safety
* Reduced wildlife accidents
* Real-time animal detection system
* Reliable non-visual sensing approach

---

## Future Improvements

* Integration with real CSI hardware
* Deep learning models for improved accuracy
* IoT based roadside deployment
* Mobile alert system for drivers
* Cloud based monitoring dashboard

---

## Authors

Ravi Kumar

Rinku

Sonu Bhai Patel

B.Tech Software Engineering Project
