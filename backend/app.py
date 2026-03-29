from flask import Flask, render_template, jsonify
import numpy as np

from utils.preprocessing import normalize_signal
from utils.feature_extraction import extract_features
from ml.predict import predict


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


# 🔥 NEW DYNAMIC SIGNAL GENERATOR (Fix for graph issue)
def generate_signal():

    t = np.linspace(0, 10, 100)

    base = np.sin(t)

    noise = np.random.normal(0, 0.3, 100)

    variation = np.random.uniform(0.5, 2)

    signal = variation * base + noise

    return signal


def run_detection():

    signal = generate_signal()

    signal = normalize_signal(signal)

    features = extract_features(signal)

    prediction = predict(features)

    if prediction == 0:
        status = "No Animal Detected"
        color = "green"
        icon = "✅"

    elif prediction == 1:
        status = "Small Animal Detected"
        color = "red"
        icon = "🐕"

    elif prediction == 2:
        status = "Medium Animal Crossing"
        color = "red"
        icon = "🐄"

    else:
        status = "Large Animal Crossing"
        color = "red"
        icon = "🐘"

    return signal.tolist(), status, color, icon


@app.route("/")
def dashboard():

    signal, status, color, icon = run_detection()

    return render_template(
        "dashboard.html",
        signal=signal,
        status=status,
        color=color,
        icon=icon
    )


@app.route("/detect")
def detect():

    signal, status, color, icon = run_detection()

    return jsonify({
        "signal": signal,
        "status": status,
        "color": color,
        "icon": icon
    })


if __name__ == "__main__":
    app.run(debug=True)
