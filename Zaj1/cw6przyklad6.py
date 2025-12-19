#dla sygnałów muzycznych można spróbować oszacować etapy ADSR (attack, decay, sustain, release). spróbuj wyznaczyć obiwednię amplitudy sygnału piano_a4.wav używając funkcji hilberta i wyświetl ją na wykresie razem z sygnałem oryginalnym

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile
from scipy.signal import get_window

from scipy.signal import hilbert

fs, x =wavfile.read("Zaj1/piano_a4.wav") #odczyt pliku wav; fs - czestotliwość próbkowania, x - sygnał
#zamien na mono
if x.ndim > 1:
    x = x.mean(axis=1)

N= len (x) #liczba próbek sygnałuX
X= fft(x) #obliczenie transformaty fouriera
f= fftfreq(N, 1/fs) #fftfreq - wektor częstotliwości odpowiadający wartościom transformaty fouriera

t=np.arange(len(x))/fs  #t = wektor czasu, np.arrange(len(x)) tworzy wektor od 0 do długości x-1, dzielone przez fs aby uzyskać czas w sekundach
env = np.abs(hilbert(x)) #obliczenie obwiedni sygnału za pomocą transformaty Hilberta
plt.plot(t, x, label='Sygnał oryginalny')
plt.plot(t, env, label='Obwiednia amplitudy', color='red')
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.title("Obwiednia sygnału ADSR")
plt.legend()
plt.show()