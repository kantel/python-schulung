import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 2, 0.01)
s = np.sin(2*np.pi*t)
c = np.cos(2*np.pi*t)

plt.plot(t, s)
plt.plot(t, c)

plt.show()
