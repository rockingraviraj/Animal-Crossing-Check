import numpy as np

def generate_signal():

    t = np.linspace(0,10,100)

    signal = np.sin(t)

    noise = np.random.normal(0,0.2,100)

    signal = signal + noise

    return signal


def apply_fft(signal):

    fft_values = np.fft.fft(signal)

    magnitude = np.abs(fft_values)

    return magnitude