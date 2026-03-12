import numpy as np

def moving_average(signal, window=5):
    return np.convolve(signal, np.ones(window)/window, mode='same')

def apply_fft(signal):
    return np.abs(np.fft.fft(signal))