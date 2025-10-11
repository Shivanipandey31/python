import  matplotlib.pyplot as plt
import numpy as np 
# x=np.arange(1,10)
# y=np.arange(75,84)
# plt.plot(x,y,'o')
# plt.show()

# x=np.array([1,2,3,45])
y=np.array([1,99,0,4,9,45,31])
x=y[::-1]
plt.plot(y,marker='*',ms=50,mfc='blue', mec='orange',ls='-.',c='blue',lw='1')
plt.plot(x,marker='o',ms=50,mfc='orange', mec='blue',ls='-.',c='orange',lw='1')
plt.grid(axis='x')
plt.show()