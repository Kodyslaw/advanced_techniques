import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq

def load(path):
    fs, x = wavfile.read(path)
    return fs, x.astype(float)/np.max(np.abs(x))

def centroid(x, fs):
    N = len(x)
    X = np.abs(fft(x))[:N//2]        # FFT → widmo amplitudowe tylko dodatnie częstotliwości
    f = fftfreq(N, 1/fs)[:N//2]      # wektor częstotliwości dopasowany do FFT
    return np.sum(f*X)/np.sum(X)     # środek masy widma

for f in [r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\tone_440.wav", r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\tone_noisy.wav"]:
    fs,x = load(f)
    print(f, centroid(x,fs))