#do oceny jakości rekonstrukcji używamy rms błędu i analizy histogramu
#do rekonstruckji z zadanie44.pyy oblicz RMS błędu, narysuj histogram, oveń subiektywnie jaokość sygnału

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq, ifft
from scipy.signal.windows import hamming
from scipy import signal

fs, x =wavfile.read("Zaj1/twotones.wav")
x =x.astype(float) / np.max(np.abs(x)) #normalizacja sygnału
def custom_resample(signal, old_fs, new_fs):
    return signal[::(old_fs//new_fs)]
downsample_rates = [4000, 2000]
reconstructed_signals = []
for new_fs in downsample_rates:
    x_ds= custom_resample(x, fs, new_fs)
    num_samples = len(x)  # rekonstruuj do oryginalnej liczby próbek
    x_reconstructed = signal.resample(x_ds, num_samples)  # rekonstrukcja sygnału do oryginalnej liczby próbek
    reconstructed_signals.append(x_reconstructed)
    #oblicz RMS błąd
    rms_error = np.sqrt(np.mean((x - x_reconstructed) ** 2))
    print(f"RMS błąd dla downsamplingu do {new_fs}Hz: {rms_error}")
    #rysuj histogram błędu
    error = x[:len(x_reconstructed)] - x_reconstructed
    plt.figure()
    plt.hist(error, bins=50, alpha=0.7, color='blue')
    plt.title(f"Histogram błędu dla downsamplingu do {new_fs}Hz")
    plt.xlabel("Błąd")
    plt.ylabel("Liczba próbek")
    plt.show()
    #subiektywna ocena jakości sygnału
    plt.figure()
    plt.plot(x_reconstructed)
    plt.title(f"Sygnał zrekonstruowany z downsamplingu do {new_fs}Hz")
    plt.xlabel("Próbki")
    plt.ylabel("Amplituda")
    plt.show()
    wavfile.write(f"reconstructed_{new_fs}Hz.wav", fs, (x_reconstructed * 32767).astype(np.int16))
