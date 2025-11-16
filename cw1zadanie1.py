#wytnij z sygnalu tone_440.wav sygnal o długości 1 sekundy, wyświetl go na wykresie
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
fs, x =wavfile.read("piano_a4.wav")
x=x/np.max(np.abs(x)) #normalizacja sygnału do zakresu -1 do 1
#wycięcie pierwszej sekundy sygnału
x=x[0:fs*1]
t=np.arange(len(x))/fs
plt.plot(t,x)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.title("Sygnał w dziedzinie czasu")
plt.show()
