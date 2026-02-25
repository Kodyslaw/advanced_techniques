import numpy as np
from scipy.io import wavfile

def load(path):
    fs, x = wavfile.read(path)
    return x.astype(float) / np.max(np.abs(x))

def RMS(x):
    return np.sqrt(np.mean(x**2))   # definicja RMS = pierwiastek z średniej kwadratów

files = [r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\tone_440.wav", r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\tone_noisy.wav", r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\twotones.wav"]


for f in files:
    print(f, RMS(load(f)))