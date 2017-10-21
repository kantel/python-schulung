import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10., 10., 1000)
plt.plot(x, np.sin(x), "-r", label="Sinus")
plt.plot(x, np.cos(x), "-b", label="Cosinus")
plt.legend()
plt.ylim(-2., 2.)
plt.grid()
plt.show()
