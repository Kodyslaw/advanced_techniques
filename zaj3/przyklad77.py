import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft

# wczytanie sygnału
fs, x = wavfile.read("Zaj1/twotones.wav")
x = x.astype(float)
x = x / np.max(np.abs(x))

# fragmenty o różnej długości
segments = [x[:2000], x[:10000], x[:20000]]

plt.figure(figsize=(10, 6))

for seg in segments:
    X = fft(seg)
    plt.plot(np.abs(X[:len(seg)//2]), label=f"N = {len(seg)}")

plt.title("Widmo dla różnych długości sygnału")
plt.xlabel("Próbki częstotliwości")
plt.ylabel("Amplituda")
plt.legend()
plt.grid()
plt.show()
