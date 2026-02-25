import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
from scipy.signal import find_peaks

def load(path):
    fs, x = wavfile.read(path)
    return fs, x.astype(float)/np.max(np.abs(x))

def tristimulus(x,fs):
    N=len(x)
    X=np.abs(fft(x))[:N//2]

    peaks,_=find_peaks(X,height=np.max(X)*0.05)   # wykrycie harmonicznych powyżej 5% max amplitudy
    amps=X[np.sort(peaks)]                         # amplitudy harmonicznych w kolejności częstotliwości

    if len(amps)<5:
        amps=np.pad(amps,(0,5-len(amps)))          # dopełnienie zerami aby uniknąć indeksów poza zakresem

    T1=amps[0]
    T2=np.sum(amps[1:4])
    T3=np.sum(amps[4:])
    S=T1+T2+T3

    return T1/S,T2/S,T3/S

for f in [r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\tone_440.wav", r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\tone_noisy.wav"]:
    fs,x=load(f)
    print(f, tristimulus(x,fs))