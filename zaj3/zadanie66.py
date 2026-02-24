import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt, resample
from scipy.fft import fft, fftfreq

# wczytanie sygnału
fs, x = wavfile.read("Zaj1/twotones.wav")  # fs = czestotliwosc probkowania
x = x.astype(float)  # konwersja na float do obliczen
x = x / np.max(np.abs(x))  # normalizacja amplitudy

factor = 10  # wspolczynnik decymacji
fs_ds = fs // factor  # nowe fs po downsamplingu

# --- BEZ FILTRU ---
x_ds_nf = x[::factor]  # proste probkowanie co N-ta probke (aliasing)
x_rec_nf = resample(x_ds_nf, len(x))  # rekonstrukcja do dlugosci oryginalu

# --- Z FILTREM ---
b, a = butter(6, 0.2)  # filtr dolnoprzepustowy Butterwortha rzedu 6
x_f = filtfilt(b, a, x)  # filtracja bez przesuniecia fazy
x_ds_f = x_f[::factor]  # decymacja po filtracji antyaliasingowej
x_rec_f = resample(x_ds_f, len(x))  # rekonstrukcja sygnalu

# RMS błędy
rms_nf = np.sqrt(np.mean((x - x_rec_nf) ** 2))  # blad bez filtru
rms_f = np.sqrt(np.mean((x - x_rec_f) ** 2))  # blad z filtrem

print(f"RMS bez filtru: {rms_nf}")
print(f"RMS z filtrem:  {rms_f}")

# widma
N = len(x)  # liczba probek
f = fftfreq(N, 1/fs)  # os czestotliwosci

X = fft(x)  # widmo oryginalu
X_nf = fft(x_rec_nf)  # widmo rekonstrukcji bez filtru
X_f = fft(x_rec_f)  # widmo rekonstrukcji z filtrem

plt.figure(figsize=(12, 8))

plt.subplot(2,1,1)
plt.plot(f[:N//2], np.abs(X_nf[:N//2]), label="Bez filtru")  # polowa widma
plt.plot(f[:N//2], np.abs(X[:N//2]), '--', label="Oryginał")
plt.title("Widmo – rekonstrukcja BEZ filtru")
plt.legend()
plt.grid()

plt.subplot(2,1,2)
plt.plot(f[:N//2], np.abs(X_f[:N//2]), label="Z filtrem")
plt.plot(f[:N//2], np.abs(X[:N//2]), '--', label="Oryginał")
plt.title("Widmo – rekonstrukcja Z filtrem")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()