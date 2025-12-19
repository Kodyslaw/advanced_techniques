#celem ćwiczenia jest obliczenie i przedstawienie widma amplitudowego sygnału przy użyciu transforamty fouriera
#zmodyfikuj kod tak aby wyświetlić widmo dla różnych długości fragmentów sygnału tak aby rodzaielczość wynosiła 1hz, 2hz i 4hz. porównaj szerokośc pliku odpowiadającego głównego częstotliwosci.

#przykład: 
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile

fs, x =wavfile.read("Zaj1/piano_a4.wav") #odczyt pliku wav; fs - czestotliwość próbkowania, x - sygnał

N= len (x) #liczba próbek sygnałuX
X= fft(x) #obliczenie transformaty fouriera
f= fftfreq(N, 1/fs) #fftfreq - wektor częstotliwości odpowiadający wartościom transformaty fouriera

#wyświetl widmo dla różnych długości fragmentów sygnału

plt.figure(figsize=(12,8))
plt.subplot(4,1,1)
plt.plot(f[:N//2], np.abs(X[:N//2])) # : przed N//2 oznacza "slice separator" czyli bierzemy elementy od początku do N//2
plt.title("Widmo amplitudowe sygnału - pełna długość")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.grid(True)
#dla rozdzielczości 1 Hz, potrzebna długość sygnału to fs/1
L1 = fs // 1
plt.subplot(4,1,2)
plt.plot(f[:L1//2], np.abs(X[:L1//2]))
plt.title("Widmo amplitudowe sygnału - rozdzielczość 1 Hz")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.grid(True)
#dla rozdzielczości 2 Hz, potrzebna długość sygnału to fs/2
L2 = fs // 2
plt.subplot(4,1,3)
plt.plot(f[:L2//2], np.abs(X[:L2//2]))
plt.title("Widmo amplitudowe sygnału - rozdzielczość 2 Hz")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.grid(True)
plt.tight_layout()


#dla rozdzielczości 4 Hz, potrzebna długość sygnału to fs/4
L4 = fs // 4
plt.subplot(4,1,4)
plt.plot(f[:L4//2], np.abs(X[:L4//2]))
plt.title("Widmo amplitudowe sygnału - rozdzielczość 4 Hz")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.grid(True)
plt.tight_layout()
plt.show()



#plt.plot(f[:N//2], np.abs(X[:N//2])) #wykres widma amplitudowego (tylko dodatnie częstotliwości); (f[:N//2] - wektor częstotliwości od 0 do fs/2; np.abs(X[:N//2]) - wartości absolutne (dodanie) transformaty fouriera od 0 do fs/2

#plt.xlabel("Częstotliwość [Hz]")
#plt.ylabel("Amplituda")
#plt.title("Widmo amplitudowe sygnału")
#plt.show()