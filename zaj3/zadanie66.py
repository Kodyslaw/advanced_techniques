import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import butter, filtfilt, resample
from scipy.fft import fft, fftfreq

# wczytanie sygnału
fs, x = wavfile.read("Zaj1/twotones.wav")
x = x.astype(float)
x = x / np.max(np.abs(x))

factor = 10
fs_ds = fs // factor

# --- BEZ FILTRU ---
x_ds_nf = x[::factor]
x_rec_nf = resample(x_ds_nf, len(x))

# --- Z FILTREM ---
b, a = butter(6, 0.2)
x_f = filtfilt(b, a, x)
x_ds_f = x_f[::factor]
x_rec_f = resample(x_ds_f, len(x))

# RMS błędy
rms_nf = np.sqrt(np.mean((x - x_rec_nf) ** 2))
rms_f = np.sqrt(np.mean((x - x_rec_f) ** 2))

print(f"RMS bez filtru: {rms_nf}")
print(f"RMS z filtrem:  {rms_f}")

# widma
N = len(x)
f = fftfreq(N, 1/fs)

X = fft(x)
X_nf = fft(x_rec_nf)
X_f = fft(x_rec_f)

plt.figure(figsize=(12, 8))

plt.subplot(2,1,1)
plt.plot(f[:N//2], np.abs(X_nf[:N//2]), label="Bez filtru")
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
