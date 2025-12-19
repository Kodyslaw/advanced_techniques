import numpy as np 
from scipy.io.wavfile import write

fs= 44100 #cześtotliwośc próbkowania w hz
t= np.linspace(0,2, int(fs*2), endpoint=False) #czas trwania 2 sekundy
x = 0.5*np.sin(2*np.pi*440*t) #sygnał 440hz
write("tone_440.wav", fs, (x*32767).astype(np.int16)) #zapis do pliku wav


