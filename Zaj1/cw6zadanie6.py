#zmodyfikuj kod z cw5przyklad6.py tak aby wydzielić cztery fazy ADSR analizując kształt obwiedni sygnału. zacznacz granicze faz pionowymii liniami na wykresie

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile
from scipy.signal import hilbert
fs, x =wavfile.read("Zaj1/piano_a4.wav") #odczyt pliku wav; fs - czestotliwość próbkowania, x - sygnał
#zamien na mono
if x.ndim > 1:
    x = x.mean(axis=1)

# upewnij się, że sygnał jest w formacie float
x = x.astype(float)

# sygnał analityczny i surowa obwiednia
analytic = hilbert(x)
env = np.abs(analytic)

# wygładzenie obwiedni za pomocą średniej ruchomej
win_ms = 10
win_len = max(1, int(win_ms * 1e-3 * fs))
kernel = np.ones(win_len) / win_len
env_smooth = np.convolve(env, kernel, mode='same')

t=np.arange(len(x))/fs  #t = wektor czasu, np.arrange(len(x)) tworzy wektor od 0 do długości x-1, dzielone przez fs aby uzyskać czas w sekundach

#obliczenie obwiedni sygnału za pomocą transformaty Hilberta
#env = np.abs(hilbert(x))   
plt.plot(t, x, label='Sygnał oryginalny')
plt.plot(t, env_smooth, label='Obwiednia amplitudy (wygładzona)', color='red')
#wyznaczenie faz ADSR
#start attack
attack_start = 0
#peak attack
attack_peak = np.argmax(env_smooth)
#end decay / start sustain
decay_end = attack_peak + np.where(env_smooth[attack_peak:] <= 0.7 * env_smooth[attack_peak])[0][0]
#end sustain / start release
sustain_end = decay_end + np.where(env_smooth[decay_end:] <= 0.1 * env_smooth[attack_peak])[0][0]
#end release
release_end = len(env_smooth) - 1
#rysowanie pionowych linii oznaczających fazy ADSR
plt.axvline(x=t[attack_start], color='green', linestyle='--', label='Start Attack')
plt.axvline(x=t[attack_peak], color='orange', linestyle='--', label='Peak Attack/ Start Decay')
plt.axvline(x=t[decay_end], color='purple', linestyle='--', label='End Decay / Start Sustain')
plt.axvline(x=t[sustain_end], color='brown', linestyle='--', label='End Sustain / Start Release')
plt.axvline(x=t[release_end], color='black', linestyle='--', label='End Release')
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.title("Obwiednia sygnału ADSR z zaznaczonymi fazami")
plt.legend()
plt.show()

