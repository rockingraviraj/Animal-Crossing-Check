import numpy as np
from utils.signal_processing import apply_fft

def extract_features(sample):
    features = []

    for i in range(sample.shape[1]):
        sub = sample[:, i]

        mean = np.mean(sub)
        var = np.var(sub)
        peak = np.max(sub)
        energy = np.sum(sub**2)

        fft_vals = apply_fft(sub)
        fft_energy = np.sum(fft_vals)

        features.extend([mean, var, peak, energy, fft_energy])

    return features