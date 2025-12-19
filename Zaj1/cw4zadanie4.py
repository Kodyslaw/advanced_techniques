#zmodyfikuj kod z cw4przyklad4.py tak aby zastosować skalę logartytmiczną i ograniczyć zakres częstotliwości od 20hz do 10kHz i wyświetlić jedynie dodatnie częstotliwości

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile
from scipy.signal import get_window

fs, x =wavfile.read("Zaj1/tone_440.wav") #odczyt pliku wav; fs - czestotliwość próbkowania, x - sygnał
N= len (x) #liczba próbek sygnałuX
X= fft(x) #obliczenie transformaty fouriera
f= fftfreq(N, 1/fs) #fftfreq - wektor częstotliwości odpowiadający wartościom transformaty fouriera
#ograniczenie zakresu częstotliwości od 20Hz do 10kHz
mask = (f >= 20) & (f <= 10000)

plt.semilogx(f[mask], 20*np.log10(np.abs(X[mask])+ 1e-12)) #wykres widma amplitudowego w skali logarytmicznej (tylko dodatnie częstotliwości); (f[:N//2] - wektor częstotliwości od 0 do fs/2; np.abs(X[:N//2]) - wartości absolutne (dodanie) transformaty fouriera od 0 do fs/2; 20*np.log10(...) - konwersja na skalę dB, dodanie 1e-12 aby uniknąć log(0)
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda [dB]")
plt.title("Widmo amplitudowe sygnału w skali logarytmicznej (20Hz - 10kHz)")
plt.show()

