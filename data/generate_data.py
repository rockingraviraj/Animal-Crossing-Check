import numpy as np
import pandas as pd

def simulate_signal(label):

    t = np.linspace(0,10,100)

    base_signal = np.sin(t)

    noise = np.random.normal(0,0.1,100)

    signal = base_signal + noise

    # disturbance based on animal size
    if label == 1:
        signal += np.random.normal(0,0.2,100)

    if label == 2:
        signal += np.random.normal(0,0.4,100)

    if label == 3:
        signal += np.random.normal(0,0.6,100)

    return signal


def extract_features(signal):

    mean = np.mean(signal)
    std = np.std(signal)
    max_val = np.max(signal)
    min_val = np.min(signal)
    energy = np.sum(signal**2)

    return [mean,std,max_val,min_val,energy]


data = []

samples = 1200

for i in range(samples):

    label = np.random.randint(0,4)

    signal = simulate_signal(label)

    features = extract_features(signal)

    features.append(label)

    data.append(features)


columns = ["mean","std","max","min","energy","label"]

df = pd.DataFrame(data,columns=columns)

df.to_csv("data/csi_dataset.csv",index=False)

print("CSI dataset generated successfully")