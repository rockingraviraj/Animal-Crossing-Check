from flask import Flask, render_template, jsonify
import matplotlib.pyplot as plt
# from utils.logger import log_detection

from utils.signal_simulator import generate_signal
from utils.preprocessing import normalize_signal
from utils.feature_extraction import extract_features
from ml.predict import predict


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


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
        
    # log_detection(status)
    # graph
    plt.figure(figsize=(8,3))
    plt.plot(signal)
    plt.title("CSI Signal Activity")

    graph_path = "static/signal.png"

    plt.savefig(graph_path)
    plt.close()

    return status, color, icon, graph_path


@app.route("/")
def dashboard():

    status, color, icon, graph = run_detection()

    return render_template(
        "dashboard.html",
        status=status,
        color=color,
        icon=icon,
        graph=graph
    )


@app.route("/detect")
def detect():

    status, color, icon, graph = run_detection()

    return jsonify({
        "status": status,
        "color": color,
        "icon": icon,
        "graph": graph
    })


if __name__ == "__main__":
    app.run(debug=True)
