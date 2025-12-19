#zmodyfikuj kod z pliku cw5przyklad5.py tak aby podzielić sygnał na 8 okien z 50% nakładaniem i obliczyć widmo dla każdego z okien, wyniki Zapisz wyniki w tablicy 2d (czestotliwość / czas)

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile
from scipy.signal import get_window
fs, x =wavfile.read("Zaj1/piano_a4.wav") #odczyt pliku wav; fs - czestotliwość próbkowania, x - sygnał
N= len (x) #liczba próbek sygnałuX
X= fft(x) #obliczenie transformaty fouriera
f= fftfreq(N, 1/fs) #fftfreq - wektor częstotliwości odpowiadający wartościom transformaty fouriera

n = 4
segments =np.array_split(x, n) #podział sygnału x na n równych fragmentów
overlap = len(segments[0]) // 2  # 50% nakładanie
spectra = []  # tablica 2D do przechowywania widm
for i in range(n):
    start = i * (len(segments[0]) - overlap)
    end = start + len(segments[0])
    seg = x[start:end]
    if len(seg) < len(segments[0]):
        seg = np.pad(seg, (0, len(segments[0]) - len(seg)), 'constant')  # dopełnienie zerami jeśli fragment jest krótszy
    Xs =np.abs(fft(seg)) #obliczenie transformaty fouriera dla fragmentu sygnału
    spectra.append(Xs)
    f_seg = fftfreq(len(seg), 1/fs) #obliczenie wektora częstotliwości dla fragmentu
    plt.plot(f_seg[:len(seg)//2], 20*np.log10(Xs[:len(seg)//2]+1e-12), label=f"okno {i+1}") #wykres widma amplitudowego w skali logarytmicznej (tylko dodatnie częstotliwości); (f_seg[:len(seg)//2] - wektor częstotliwości od 0 do fs/2 dla fragmentu; np.abs(Xs[:len(seg)//2]) - wartości absolutne (dodanie) transformaty fouriera od 0 do fs/2 dla fragmentu; 20*np.log10(...) - konwersja na skalę dB, dodanie 1e-12 aby uniknąć log(0)
spectra = np.array(spectra)  # konwersja listy na tablicę 2D
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda [dB]")
plt.legend()
plt.title("Widmo amplitudowe dla podzielonych fragmentów sygnału z 50% nakładaniem")
plt.show()

print(spectra)