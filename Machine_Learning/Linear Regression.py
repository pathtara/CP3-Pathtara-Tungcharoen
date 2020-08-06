import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-5, 5, 100)
y = 2*x + 1
plt.plot(x, y,'-r', label = 'y = 2x+1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc = "upper left")
plt.title("2x+1")
plt.grid()
plt.show()