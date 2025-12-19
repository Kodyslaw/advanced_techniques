import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt, resample
from scipy.fft import fft, fftfreq

# wczytanie sygnału
fs, x = wavfile.read("Zaj1/twotones.wav")
x = x.astype(float)
x = x / np.max(np.abs(x))

# filtr dolnoprzepustowy
b, a = butter(6, 0.2)
x_f = filtfilt(b, a, x)

# downsampling
factor = 10
x_ds = x_f[::factor]
fs_ds = fs // factor

# rekonstrukcja
x_rec = resample(x_ds, len(x))

# widma
N = len(x)
X = fft(x)
X_rec = fft(x_rec)
f = fftfreq(N, 1/fs)

plt.figure(figsize=(10, 6))
plt.plot(f[:N//2], np.abs(X[:N//2]), label="Oryginał")
plt.plot(f[:N//2], np.abs(X_rec[:N//2]), '--', label="Zrekonstruowany")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.title("Widmo")
plt.legend()
plt.grid()
plt.show()
