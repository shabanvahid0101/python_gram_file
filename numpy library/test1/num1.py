import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 30, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.axis([0, 30, -1.1, 1.1])  # set axis limits
plt.show()