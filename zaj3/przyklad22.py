#twotones zawiera skladowae 440hz i 1000hz, downsampling ujawni aliasy
# co się ma pokazać? ton 440hz jest ok. ton 1000hz aliasuje do 1000-4000 = -3000hz -> wartosc bezwzgledna 3000hz, ale ponieważ 300hz > niż nyquist 2000hz, aliasuje sie dalej aż trafi w pasmo

from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
import numpy as np

fs, x =wavfile.read("Zaj1/twotones.wav")
x =x.astype(float) / np.max(np.abs(x)) #normalizacja sygnału do zakresu -1 do 1

def resample(signal, old_fs, new_fs):
    
    return signal[::(old_fs//new_fs)]
x2= resample(x, fs, 4000)
fs2= 4000

X= fft(x2) #obliczenie transformaty fouriera
f=fftfreq(len(X), 1/fs2) #fftfreq - wektor częstotliwości odpowiadający wartościom transformaty fouriera

plt.plot(f[:len(X)//2], np.abs(X[:len(X)//2])) #wykres widma amplitudowego (tylko dodatnie częstotliwości); (f[:N//2] - wektor częstotliwości od 0 do fs/2; np.abs(X[:N//2]) - wartości absolutne (dodanie) transformaty fouriera od 0 do fs/2
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.title("Widmo amplitudowe sygnału po downsamplingu do 4khz")
plt.show()  
