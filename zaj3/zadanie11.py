#zmodyfikuj kod z przyklad11.py tak aby zrobić downsamplink do 8khz, 4khz i 2khz oraz wyświetlić widmo oryginalnego i zdownsamplowanego sygnału na czterech subplotach. dla każej wersji wykonaj FFT i porównaj zmiany w widmie. FFT wyświetl w osobnym oknie

from matplotlib import pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
import numpy as np

fs, x =wavfile.read("Zaj1/tone_440.wav")
x=x.astype(float) / np.max(np.abs(x)) #normalizacja sygnału do zakresu -1 do 1
downsample_factors = [1, 5, 10, 20]  # odpowiadające 44.1kHz, 8.82kHz, 4.41kHz, 2.205kHz
plt.figure(figsize=(10, 8))


for i, factor in enumerate(downsample_factors):
    x_ds= x[::factor] #downsampling - wybieranie co 'factor' próbkę
    fs_ds=fs//factor #nowa częstotliwość próbkowania
    N= len (x_ds) #liczba próbek sygnałuX
    X= fft(x_ds) #obliczenie transformaty fouriera
    f= fftfreq(N, 1/fs_ds) #fftfreq - wektor częstotliwości odpowiadający wartościom transformaty fouriera

    plt.subplot(2, 2, i+1)
    plt.plot(f[:N//2], np.abs(X[:N//2])) #wykres widma amplitudowego (tylko dodatnie częstotliwości); (f[:N//2] - wektor częstotliwości od 0 do fs/2; np.abs(X[:N//2]) - wartości absolutne (dodanie) transformaty fouriera od 0 do fs/2
    plt.xlabel("Częstotliwość [Hz]")
    plt.ylabel("Amplituda")
    if factor == 1:
        plt.title("Widmo oryginalnego sygnału (44.1kHz)")
    else:
        plt.title(f"Widmo sygnału po downsamplingu do {fs_ds/1000:.2f}kHz")



plt.tight_layout()
plt.show()
