import joblib
import numpy as np

# trained model load karo
model = joblib.load("models/model.pkl")

# sample signal value
sample_signal = np.array([[0.8]])

# prediction
prediction = model.predict(sample_signal)

# result print karo
if prediction[0] == 1:
    print("Animal Detected")
else:
    print("No Animal Detected")