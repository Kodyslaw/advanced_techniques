#spróbkuj twotones.wav w 6000hz, 3000hz i 1500hz, wyświetl widma dla każdego z nich i porównaj aliasowanie

from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
import numpy as np

fs, x =wavfile.read("Zaj1/twotones.wav")
x =x.astype(float) / np.max(np.abs(x)) #normalizacja sygnału do zakresu -1 do 1
def resample(signal, old_fs, new_fs):
    return signal[::(old_fs//new_fs)]
downsample_rates = [6000, 3000, 1500]
plt.figure(figsize=(10, 8))

for i, new_fs in enumerate(downsample_rates):
    x_ds= resample(x, fs, new_fs)
    N= len (x_ds) #liczba próbek sygnałuX
    X= fft(x_ds) #obliczenie transformaty fouriera
    f=fftfreq(N, 1/new_fs) #fftfreq - wektor częstotliwości odpowiadający wartościom transformaty fouriera

    plt.subplot(3, 1, i+1)
    plt.plot(f[:N//2], np.abs(X[:N//2])) #wykres widma amplitudowego (tylko dodatnie częstotliwości); (f[:N//2] - wektor częstotliwości od 0 do fs/2; np.abs(X[:N//2]) - wartości absolutne (dodanie) transformaty fouriera od 0 do fs/2
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Amplituda")
    plt.title(f"Widmo sygnału po downsamplingu do {new_fs}Hz")
plt.tight_layout()
plt.show()
