import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq

def load(path):
    fs, x = wavfile.read(path)
    return fs, x.astype(float)/np.max(np.abs(x))

def brightness(x,fs,fc=1500):
    N=len(x)
    X=np.abs(fft(x))[:N//2]
    f=fftfreq(N,1/fs)[:N//2]
    return np.sum(X[f>fc])/np.sum(X)   # stosunek energii powyżej progu do całej energii

fs,x=load(r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\tone_noisy.wav")
print(brightness(x,fs))