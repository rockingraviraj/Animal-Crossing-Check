import numpy as np
from utils.signal_simulator import apply_fft

def extract_features(signal):

    fft_signal = apply_fft(signal)

    mean = np.mean(fft_signal)
    std = np.std(fft_signal)
    max_val = np.max(fft_signal)
    min_val = np.min(fft_signal)
    energy = np.sum(fft_signal**2)

    features = [mean,std,max_val,min_val,energy]

    return features