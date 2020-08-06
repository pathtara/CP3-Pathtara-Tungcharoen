import numpy as np
import matplotlib.pyplot as plt

rng = np.random
x = rng.rand(50)*10

y = (2*x)**2 + rng.randn(50)

plt.scatter(x,y)
plt.show()
