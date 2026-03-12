import numpy as np
import os

def generate_csi_sample(animal_type, time_steps=200, subcarriers=30):
    base_signal = np.random.normal(0, 0.2, (time_steps, subcarriers))

    if animal_type == "small":
        disturbance = np.sin(np.linspace(0, 8, time_steps)) * 0.5
    elif animal_type == "medium":
        disturbance = np.sin(np.linspace(0, 8, time_steps)) * 1.0
    else:
        disturbance = np.sin(np.linspace(0, 8, time_steps)) * 2.0

    disturbance = disturbance.reshape(-1, 1)
    signal = base_signal + disturbance

    noise = np.random.normal(0, 0.1, signal.shape)
    signal += noise

    return signal

def create_dataset(samples_per_class=200):
    X = []
    y = []

    for label in ["small", "medium", "large"]:
        for _ in range(samples_per_class):
            X.append(generate_csi_sample(label))
            y.append(label)

    return np.array(X), np.array(y)

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    X, y = create_dataset()
    np.save("data/X.npy", X)
    np.save("data/y.npy", y)
    print("Dataset Generated Successfully!")