#downsampling - zagłębiennie się

from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
import numpy as np

fs, x =wavfile.read("Zaj1/tone_440.wav")
x=x.astype(float) / np.max(np.abs(x)) #normalizacja sygnału do zakresu -1 do 1

x_ds= x[::10] #downsampling - wybieranie co 10 próbkę
fs_ds=fs//10 #nowa częstotliwość próbkowania
N= len (x_ds) #liczba próbek sygnałuX
X= fft(x_ds) #obliczenie transformaty fouriera
f= fftfreq(N, 1/fs_ds) #fftfreq - wektor częstotliwości odpowiadający wartościom transformaty fouriera

plt.plot(f[:N//2], np.abs(X[:N//2])) #wykres widma amplitudowego (tylko dodatnie częstotliwości); (f[:N//2] - wektor częstotliwości od 0 do fs/2; np.abs(X[:N//2]) - wartości absolutne (dodanie) transformaty fouriera od 0 do fs/2

plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.title("Widmo amplitudowe sygnału po downsamplingu do 4khz")
plt.show()
