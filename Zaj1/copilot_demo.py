# Narysuj wykres sinusoidy 0-2pi
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import pytest


x = np.linspace(0, 2 * np.pi, 100) #zwraca równo rozłożone cyfry od 0 do 2* PI, 100 sampli
y = np.sin(x) #zwraca sinus od x
plt.plot(x, y) #generuje wykres z wartościami x i y
plt.title('Wykres Sinusoidy od 0 do 2π') #tytuł wykresu
plt.xlabel('Kąt (radiany)') #opis osi x
plt.ylabel('sin(x)') #opis osi y
plt.grid(True) #włączenie siatki na wykresie
plt.show() #pokazanie całości
