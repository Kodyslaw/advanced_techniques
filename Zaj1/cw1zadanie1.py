#wytnij z sygnalu piano_a4.wav sygnal o długości 1 sekundy, wyświetl go na wykresie
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
fs, x =wavfile.read("Zaj1/piano_a4.wav") #odczyt pliku wav; fs - czestotliwość próbkowania, x - sygnał
x=x/np.max(np.abs(x)) #normalizacja sygnału do zakresu -1 do 1
#wycięcie pierwszej sekundy sygnału
x=x[0:fs*1] #x od 0 do fs*1 (czestotliwosc próbkowania * 1 sekunda)
t=np.arange(len(x))/fs  #t = wektor czasu, np.arrange(len(x)) tworzy wektor od 0 do długości x-1, dzielone przez fs aby uzyskać czas w sekundach
plt.plot(t,x) #wykres, wektor czasu na osi x, sygnał skrócony do 1 sekundy na osi y
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.title("Sygnał w dziedzinie czasu")
plt.show()
