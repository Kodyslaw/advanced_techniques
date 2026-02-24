import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq

# wczytanie sygnału
fs, x = wavfile.read("Zaj1/twotones.wav")  # fs = czestotliwosc probkowania
x = x.astype(float)  # konwersja na float
x = x / np.max(np.abs(x))  # normalizacja amplitudy

# czasy trwania fragmentów [s]
durations = [0.1, 0.5, 1.0, 2.0]  # rozne dlugosci analizy

plt.figure(figsize=(12, 8))

for i, t in enumerate(durations):
    N = int(fs * t)  # liczba probek dla danego czasu
    segment = x[:N]  # wyciecie fragmentu sygnalu

    X = fft(segment)  # FFT fragmentu
    f = fftfreq(N, 1/fs)  # os czestotliwosci

    plt.subplot(2, 2, i+1)  # siatka wykresow 2x2
    plt.plot(f[:N//2], np.abs(X[:N//2]))  # tylko dodatnie czestotliwosci
    plt.title(f"Czas trwania: {t} s (N = {N})")
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Amplituda")
    plt.grid()

plt.tight_layout()  # automatyczne dopasowanie odstępów
plt.show()