import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,50)
y =np.sin(x)

plt.subplot(2, 2, 1)
plt.plot(x,y)

x = np.arange(100)
y =np.cos(x)

plt.subplot(2, 2, 2)
plt.plot(x,y)

x = np.arange(100)
y =np.exp(x)

plt.subplot(2, 2, 3)
plt.plot(x,y)

x = np.arange(100)
y =np.log(x)

plt.subplot(2, 2, 4)
plt.plot(x,y)
plt.show()

