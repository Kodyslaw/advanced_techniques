#w ramach zadania sprawdzamy jak downsampling zmienia widmo sygnału na tone_440.wav

import numpy as np
import matplotlib.pyplot as plt

fs = 1000 #częstotliwość próbkowania po downsamplingu
t =np.linspace(0,1, fs, endpoint=False) #wektor czasu 1 sekunda
x = np.sin(2*np.pi*1200*t) #sygnał próbkowany z częstotliwością 1200hz

plt.plot(t[:200], x[:200]) #wykres pierwszych 200 próbek sygnału
plt.title("aliasowanie sygnału 1200hz przy fs=1000hz")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.show() 