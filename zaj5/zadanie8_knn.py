import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks
from sklearn.neighbors import KNeighborsClassifier

def load(path):
    fs, x = wavfile.read(path)
    # dźwięk testowy jest stereo i nie chciało mi się szukać kolejnego w mono
    if x.ndim > 1:
        x = np.mean(x, axis=1)
    return fs, x.astype(float)/np.max(np.abs(x))

def features(x,fs):
    N=len(x)
    X=np.abs(fft(x))[:N//2]
    f=fftfreq(N,1/fs)[:N//2]

    zcr=len(np.where(np.diff(np.sign(x)))[0])/len(x)
    rms=np.sqrt(np.mean(x**2))
    c=np.sum(f*X)/np.sum(X)
    s=np.sqrt(np.sum(((f-c)**2)*X)/np.sum(X))
    b=np.sum(X[f>1500])/np.sum(X)

    peaks,_=find_peaks(X,height=np.max(X)*0.1)
    amps=X[np.sort(peaks)]

    if len(amps)<5:
        amps=np.pad(amps,(0,5-len(amps)))

    T1=amps[0]; T2=np.sum(amps[1:4]); T3=np.sum(amps[4:])
    S=T1+T2+T3

    return [zcr,rms,c,s,b,T1/S,T2/S,T3/S]

data=[r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\tone_440.wav", r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\tone_noisy.wav", r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\twotones.wav"]
labels=["ton","szum","ton_złożony"]

X=[]
for f in data:
    fs,x=load(f)
    X.append(features(x,fs))

knn=KNeighborsClassifier(n_neighbors=3)  # klasyfikacja na podstawie 3 najbliższych sąsiadów
knn.fit(X,labels)

fs,x=load(r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\test.wav")
print(knn.predict([features(x,fs)]))