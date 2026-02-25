import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

def load(path):
    fs, x = wavfile.read(path)
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

files=[r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\tone_440.wav", r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\tone_noisy.wav", r"R:\studia\Gniadek\zaj1\advanced_techniques\zaj5\twotones.wav"]
labels=["ton","szum","ton_złożony"]

X=[]
for f in files:
    fs,x=load(f)
    X.append(features(x,fs))

svm=SVC(kernel="rbf")   # jądro RBF pozwala oddzielać klasy nieliniowo
svm.fit(X,labels)

pred=svm.predict(X)
print(confusion_matrix(labels,pred))   # pokazuje gdzie model się myli