#downsampling powoduje aliasing, okno hamminga tłumi brzegi syugnału, to njprostrza forma filtru antyaliasingowego

from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from scipy import signal
from scipy.signal.windows import hamming
import numpy as np


fs, x =wavfile.read("Zaj1/twotones.wav")

w= hamming(len(x)) #funkcja okna hamminga
x_w= x * w #zastosowanie okna do sygnału
x_ds= x_w[::10] #downsampling - wybieranie co 10 próbkę
fs_ds=fs//10 #nowa częstotliwość próbkowania

X =fft(x_ds) #obliczenie transformaty fouriera
f=fftfreq(len(X), 1/fs_ds) #fftfreq - wektor częstotliwości odpowiadający wartościom transformaty fouriera

plt.plot(f[:len(f)//2], np.abs(X[:len(f)//2])) #wykres widma amplitudowego (tylko dodatnie częstotliwości); (f[:N//2] - wektor częstotliwości od 0 do fs/2; np.abs(X[:N//2]) - wartości absolutne (dodanie) transformaty fouriera od 0 do fs/2
plt.title("widmo sygnału po downsamplingu z oknem hamminga")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.show()