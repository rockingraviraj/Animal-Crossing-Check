from flask import Flask, render_template
import joblib
import numpy as np
import random
import matplotlib.pyplot as plt

app = Flask(__name__)

# load trained model
model = joblib.load("models/model.pkl")


@app.route("/")
def home():

    # generate simulated CSI signal
    signal_values = np.random.normal(0.5, 0.2, 100)

    # create graph
    plt.figure()
    plt.plot(signal_values)
    plt.title("CSI Signal Activity")

    graph_path = "static/signal.png"

    plt.savefig(graph_path)
    plt.close()

    # random signal for prediction
    sample_signal = np.array([[random.uniform(0, 1)]])

    prediction = model.predict(sample_signal)

    if prediction[0] == 1:
        status = "Animal Detected"
    else:
        status = "No Animal Detected"

    return render_template("dashboard.html", status=status, graph=graph_path)


if __name__ == "__main__":
    app.run(debug=True)