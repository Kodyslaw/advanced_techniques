# Narysuj wykres sinusoidy 0-2pi
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Wykres Sinusoidy od 0 do 2π')
plt.xlabel('Kąt (radiany)')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()
