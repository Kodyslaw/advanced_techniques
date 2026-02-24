import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq

# wczytanie sygnału
fs, x = wavfile.read("Zaj1/twotones.wav")
x = x.astype(float)
x = x / np.max(np.abs(x))

# czasy trwania fragmentów [s]
durations = [0.1, 0.5, 1.0, 2.0]

plt.figure(figsize=(12, 8))

for i, t in enumerate(durations):
    N = int(fs * t)
    segment = x[:N]

    X = fft(segment)
    f = fftfreq(N, 1/fs)

    plt.subplot(2, 2, i+1)
    plt.plot(f[:N//2], np.abs(X[:N//2]))
    plt.title(f"Czas trwania: {t} s (N = {N})")
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Amplituda")
    plt.grid()

plt.tight_layout()
plt.show()