#przerób kod z cw3przyklad3.py tak aby porównać widma dla trzech różnych okien na trzech różnych wykresach i opisać któe z nich najlepiej tłumi sygnały spoza głównego pasma

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile
from scipy.signal import get_window

fs, x =wavfile.read("Zaj1/tone_440.wav") #odczyt pliku wav; fs - czestotliwość próbkowania, x - sygnał
N= len (x) #liczba próbek sygnałuX
X= fft(x) #obliczenie transformaty fouriera
f= fftfreq(N, 1/fs) #fftfreq - wektor częstotliwości odpowiadający wartościom transformaty fouriera
windows=['boxcar', 'hann', 'hamming', 'blackman']
plt.figure(figsize=(10,6))

#pętla wyświetlająca każde okno na osobnym wykresie
for wname in windows:
   
    
    w =get_window(wname, N) #ustawia zmienną w jako okno o nazwie wname i długości N; get_window - funkcja zwracająca gotowe okna
    Xw = fft(x[:N] * w)  #obliczenie transformaty fouriera sygnału okienkowanego  na okno "<wname>"
    
    plt.plot(f[:N//2], 20*np.log10(np.abs(Xw[:N//2])+1e-12), label=wname) #wygenerowanie wykresu widma amplitudowego w skali dB dla okna o nazwie wname
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Amplituda [dB]")
    plt.legend()
    plt.title("Porownanie roznych funkcji okien")

plt.show()
# Analiza:
# Okno boxcar ma najmniejsze tłumienie sygnałów spoza głównego pasma, ale ma największą ilość wibracji w widmie.
# Okno Hann ma lepsze tłumienie niż boxcar, ale nadal ma pewne wibracje.
# Okno Hamming ma jeszcze lepsze tłumienie niż Hann i mniejsze wibracje.
# Okno Blackman ma najlepsze tłumienie sygnałów spoza głównego pasma i minimalne wibracje.