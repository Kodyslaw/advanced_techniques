#zastosowanie funkcji okien pozwala zmniejszyć przeciek częstotliwościowy w widmie sygnału

import numpy as np
import matplotlib.pylab as plt
from scipy.signal import get_window
from scipy.fft import fft, fftfreq
from scipy.io import wavfile

fs, x =wavfile.read("Zaj1/tone_440.wav") #odczyt pliku wav; fs - czestotliwość próbkowania, x - sygnał

N= len (x) #liczba próbek sygnałuX
f= fftfreq(N, 1/fs) #fftfreq - wektor częstotliwości odpowiadający wartościom transformaty fouriera

windows=['boxcar', 'hann', 'hamming', 'blackman']
for wname in windows:
    w =get_window(wname, N)
    Xw = fft(x[:N] * w) 
    plt.plot(f[:N//2], 20*np.log10(np.abs(Xw[:N//2])+1e-12), label=wname)

plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda [dB]")
plt.legend()
plt.title("Porownanie roznych funkcji okien")
plt.show()