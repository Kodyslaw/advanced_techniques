#weź plik twotones.wav, downsampluj go do 4khz i 2khz. zrekonstruuj sygnały metodą resample i porównaj widma i przebieg

from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
from scipy.signal import resample
import numpy as np
fs, x =wavfile.read("Zaj1/twotones.wav")
x =x.astype(float) / np.max(np.abs(x)) #normalizacja sygnału do zakresu -1 do 1
def custom_resample(signal, old_fs, new_fs):
    return signal[::(old_fs//new_fs)]
downsample_rates = [4000, 2000]
plt.figure(figsize=(10, 8))
for i, new_fs in enumerate(downsample_rates):
    x_ds= custom_resample(x, fs, new_fs)
    N= len (x_ds) #liczba próbek sygnałuX
    X= fft(x_ds) #obliczenie transformaty fouriera
    f=fftfreq(N, 1/new_fs) #fftfreq - wektor częstotliwości odpowiadający wartościom transformaty fouriera

    plt.subplot(2, 1, i+1)
    plt.plot(f[:N//2], np.abs(X[:N//2])) #wykres widma amplitudowego (tylko dodatnie częstotliwości); (f[:N//2] - wektor częstotliwości od 0 do fs/2; np.abs(X[:N//2]) - wartości absolutne (dodanie) transformaty fouriera od 0 do fs/2
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Amplituda")
    plt.title(f"Widmo sygnału po downsamplingu do {new_fs}Hz")
plt.tight_layout()
plt.show()

#rekonstrukcja sygnału metodą resample
plt.figure(figsize=(10, 6))
for i, new_fs in enumerate(downsample_rates):
    x_ds= custom_resample(x, fs, new_fs)
    num_samples = int(len(x_ds) * (fs / new_fs))  # oblicz liczbę próbek po rekonstrukcji
    x_reconstructed = resample(x_ds, num_samples)  # rekonstrukcja sygnału do oryginalnej liczby próbek

    plt.subplot(2, 1, i+1)
    plt.plot(x_reconstructed)
    plt.title(f"Sygnał zrekonstruowany z downsamplingu do {new_fs}Hz")
    plt.xlabel("Próbki")
    plt.ylabel("Amplituda")
plt.tight_layout()
plt.show()