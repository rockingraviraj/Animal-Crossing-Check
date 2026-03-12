from flask import Flask, request, jsonify
import numpy as np
import pickle
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.feature_extraction import extract_features

app = Flask(__name__)

model = pickle.load(open("models/rf_model.pkl", "rb"))
encoder = pickle.load(open("models/label_encoder.pkl", "rb"))

@app.route("/status")
def status():
    return jsonify({"status": "System Running"})

@app.route("/predict", methods=["POST"])
def predict():
    signal = np.array(request.json["signal"])
    features = extract_features(signal)
    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)
    confidence = max(model.predict_proba(features)[0])

    label = encoder.inverse_transform(prediction)[0]

    return jsonify({
        "prediction": label,
        "confidence": float(confidence)
    })

if __name__ == "__main__":
    app.run(debug=True)