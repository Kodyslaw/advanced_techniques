# wygeneruj sygnał 1500hz i spróbkuj go częśtotliwościami 800, 1500 i 44100 hz 

import numpy as np
import matplotlib.pyplot as plt

fs = [800, 1500, 44100] #częstotliwość próbkowania po downsamplingu

for liczba_fs in fs:
    
    t = np.linspace(0,1, liczba_fs, endpoint=False) #wektor czasu 1 sekunda
    x = np.sin(2*np.pi*1500*t) # generuje sygnał 1500hz
    plt.subplot(2,2, fs.index(liczba_fs)+1) #tworzenie podwykresów z różnym próbkowaniem
    plt.plot(t[:500], x[:500]) #wykres pierwszych 200 próbek sygnału
    plt.title(f"aliasowanie sygnału 1500hz przy fs={liczba_fs}hz")
    plt.xlabel("Czas [s]")
    plt.ylabel("Amplituda")
plt.tight_layout()
plt.show()

#wykres przy fs=800 wskazuje aliasowaanie i bardzo ostre punkty, sygnał jest źle odtworzony - metaliczny dźwięk
#wykres przy fs=1500 rozjeżdża się i wygląda na bardzo zniekształcony sygnał
#wykres przy fs=44100 wygląda dobrze i sygnał jest poprawnie odtworzony