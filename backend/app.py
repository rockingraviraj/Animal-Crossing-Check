from flask import Flask, render_template, jsonify
import numpy as np
import random
from flask import Response
import csv
import io

from utils.preprocessing import normalize_signal
from utils.feature_extraction import extract_features
from ml.predict import predict
from utils.stats import get_stats
from utils.stats import update_stats, get_stats
from utils.history import save_detection, get_history
from utils.stats import update_stats, get_stats


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


# 🔥 Dynamic signal generator
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

    # 🔥 Demo mode (random prediction for better output)
    prediction = random.randint(0, 3)

    confidence = random.randint(70, 95)

    # update stats
    update_stats(prediction)

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

    save_detection(status) 

    return signal.tolist(), status, color, icon, confidence


@app.route("/")
def dashboard():

    
    signal, status, color, icon, confidence = run_detection()

    return render_template(
        "dashboard.html",
        signal=signal,
        status=status,
        color=color,
        icon=icon,
        confidence=confidence
    )


@app.route("/detect")
def detect():

    signal, status, color, icon, confidence = run_detection()

    return jsonify({
        "signal": signal,
        "status": status,
        "color": color,
        "icon": icon,
        "confidence": confidence
    })


@app.route("/stats")
def stats_page():

    stats = get_stats()

    return render_template("stats.html", stats=stats)


@app.route("/history")
def history_page():

    history = get_history()

    return render_template("history.html", history=history)

@app.route("/history-data")
def history_data():

    history = get_history()

    return jsonify(history)


@app.route("/admin")
def admin():
    return render_template("admin.html")


@app.route("/stats-data")
def stats_data():
    return jsonify(get_stats())


@app.route("/export-csv")
def export_csv():

    history = get_history()

    # memory file
    output = io.StringIO()
    writer = csv.writer(output)

    # header
    writer.writerow(["Time", "Status"])

    # data
    for item in history:
        writer.writerow([item["time"], item["status"]])

    # response
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=report.csv"}
    )


if __name__ == "__main__":
    app.run(debug=True)