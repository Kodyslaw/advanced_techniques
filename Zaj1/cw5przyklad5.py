#podzial sygnalu na krtótsze fragmenty umożliwia analizę zmian widma w czasie, to wstęp do spektogramu

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile
from scipy.signal import get_window
fs, x =wavfile.read("Zaj1/twotones.wav") #odczyt pliku wav; fs - czestotliwość próbkowania, x - sygnał
N= len (x) #liczba próbek sygnałuX
X= fft(x) #obliczenie transformaty fouriera
f= fftfreq(N, 1/fs) #fftfreq - wektor częstotliwości odpowiadający wartościom transformaty fouriera

n = 8
segments =np.array_split(x, n) #podział sygnału x na n równych fragmentów

for i, seg in enumerate(segments):
    Xs =np.abs(fft(seg)) #obliczenie transformaty fouriera dla fragmentu sygnału
    f_seg = fftfreq(len(seg), 1/fs) #obliczenie wektora częstotliwości dla fragmentu
    plt.plot(f_seg[:len(seg)//2], 20*np.log10(Xs[:len(seg)//2]+1e-12), label=f"okno {i+1}") #wykres widma amplitudowego w skali logarytmicznej (tylko dodatnie częstotliwości); (f_seg[:len(seg)//2] - wektor częstotliwości od 0 do fs/2 dla fragmentu; np.abs(Xs[:len(seg)//2]) - wartości absolutne (dodanie) transformaty fouriera od 0 do fs/2 dla fragmentu; 20*np.log10(...) - konwersja na skalę dB, dodanie 1e-12 aby uniknąć log(0)

plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda [dB]")
plt.legend()
plt.title("Widmo amplitudowe dla podzielonych fragmentów sygnału")
plt.show()

#spektrum wsygnału podzielonego na krótsze fragmenty pokazuję jeden nakładający się wykres ponieważ jest to sygnał stacjonarny - dlatego wszystkie 8 segmentów jest identyczne 