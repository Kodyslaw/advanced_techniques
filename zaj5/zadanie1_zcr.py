import numpy as np
from scipy.io import wavfile

def load(path):
    fs, x = wavfile.read(path)
    x = x.astype(float)
    return x / np.max(np.abs(x))

def ZCR(x):
    signs = np.sign(x) # zamiana próbek na znaki +1/-1
    return len(np.where(np.diff(signs))[0]) / len(x)   # diff wykrywa zmiany znaku = przejścia przez zero

files = [r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\tone_440.wav", r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\tone_noisy.wav", r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\twotones.wav"]

for f in files:
    print(f, ZCR(load(f)))