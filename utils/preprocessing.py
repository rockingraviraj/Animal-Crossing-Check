import numpy as np

def normalize_signal(signal):

    signal = np.array(signal)

    min_val = np.min(signal)
    max_val = np.max(signal)

    normalized = (signal - min_val) / (max_val - min_val)

    return normalized