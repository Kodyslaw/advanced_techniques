#jak przywrócić stracone informacje spowodowane downsamplingiem? można spróbować interpolację, zwiększenie liczby próbek lub filtrację pasmową

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from scipy.signal import resample, butter, filtfilt
from scipy.io import wavfile

fs, x =wavfile.read("Zaj1/tone_440.wav") #odczyt pliku wav; fs - czestotliwość próbkowania, x - sygnał
#downsampling do 4kHz

x_ds=x[::10] #downsampling - wybieranie co 10 próbkę
x_rec = sig.resample(x_ds, len(x)) #interpolacja do pierwotnej liczby próbek

plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(x)
plt.title("Oryginalny sygnał")
plt.subplot(3, 1, 2)
plt.plot(x_ds)
plt.title("Sygnał po downsamplingu do 4kHz")
plt.subplot(3, 1, 3)
plt.plot(x_rec)
plt.title("Sygnał po interpolacji z powrotem do oryginalnej liczby próbek")
plt.tight_layout()
plt.show()

