#to samo co w przyklad33.py ale potrzebujemy dżwięku 440hz z szuumem i zrobić downsamplink do 4khz bez okna i drugi z 4khz z oknem hamminga


import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import resample_poly


fs, x = wavfile.read("tone_440.wav")

# Jeśli plik stereo → zamień na mono (uśrednienie kanałów)
if x.ndim > 1:
    x = x.mean(axis=1)

# Normalizacja amplitudy do zakresu [-1, 1]
x = x / np.max(np.abs(x))
target_fs = 4000  # docelowa częstotliwość próbkowania
decimation_factor = int(fs / target_fs)

print("Oryginalne fs:", fs)
print("Docelowe fs:", target_fs)
print("Decymacja:", decimation_factor)




x_down_no_window = x[::decimation_factor]




# długość okna = 10 * współczynnik decymacji (empirycznie)
window_len = decimation_factor * 10

# generujemy okno Hamminga
hamming_window = np.hamming(window_len)

# normalizacja okna (aby nie zmieniać amplitudy sygnału)
hamming_window /= np.sum(hamming_window)

# filtracja sygnału przez splot z oknem
x_filtered = np.convolve(x, hamming_window, mode="same")

# dopiero teraz decymacja
x_down_hamming = x_filtered[::decimation_factor]


def compute_fft(signal, fs):
    """
    Zwraca częstotliwości i widmo amplitudowe sygnału
    """

    N = len(signal)

    # FFT
    spectrum = np.fft.rfft(signal)

    # moduł
    magnitude = np.abs(spectrum)

    # skala częstotliwości
    freqs = np.fft.rfftfreq(N, d=1/fs)

    return freqs, magnitude


# widma
f1, S1 = compute_fft(x_down_no_window, target_fs)
f2, S2 = compute_fft(x_down_hamming, target_fs)




plt.figure(figsize=(12, 6))

plt.plot(f1, S1, label="Bez okna")
plt.plot(f2, S2, label="Z oknem Hamminga", alpha=0.8)

plt.title("Porównanie widm po downsamplingu do 4 kHz")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()