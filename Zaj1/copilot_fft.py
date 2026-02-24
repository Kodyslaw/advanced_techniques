"""Przykład obliczania dyskretnej transformacji Fouriera (FFT) i rysowania
widma sygnału.

Moduł generuje sygnał jako sumę dwóch sinusoid o zadanych częstotliwościach,
oblicza jego FFT przy użyciu numpy, a następnie rysuje zarówno przebieg w
dziedzinie czasu jak i widmo amplitudowe w dziedzinie częstotliwości.

Plik można uruchomić bezpośrednio, a także adaptować do analizy własnych
pozmierzeń. Komentarze w kodzie wyjaśniają poszczególne etapy.

docstring jest wygodniejszy od komentarzy ponieważ jest bardziej widoczny, łatwiej go znaleźć, łatwiej go zadeklarować i  jest badziej formalny. 
"""

import numpy as np
import matplotlib.pyplot as plt

def rms(x: np.ndarray) -> float:
    """Calculate the root‑mean‑square (RMS) value of a signal.
    …
    """
    return np.sqrt(np.mean(np.square(x)))
# przykład: sygnał składający się z dwóch sinusoid
fs = 1000          # częstotliwość próbkowania [Hz]
t = np.arange(0, 1.0, 1/fs)  # wektor czasu

# sinusoida 50 Hz i 120 Hz
f1 = 50
f2 = 120
signal = 0.7*np.sin(2*np.pi*f1*t) + 1.2*np.sin(2*np.pi*f2*t)

# obliczenie FFT
N = len(signal)
fft_vals = np.fft.fft(signal)
# utworzenie wektora częstotliwości
freqs = np.fft.fftfreq(N, d=1/fs)

# tylko dodatnie częstotliwości
idx = np.arange(N//2)

# widmo amplitudowe
amplitude = 2.0/N * np.abs(fft_vals[idx])

# rysowanie wykresu
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(t, signal)
plt.title('Sygnał w dziedzinie czasu')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')

plt.subplot(2,1,2)
plt.stem(freqs[idx], amplitude)
plt.title('Widmo sygnału (amplituda)')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')
plt.tight_layout()
plt.show()
#kod wygenerowany przez copilot 