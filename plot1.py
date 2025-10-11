#PLOT1
# import matplotlib.pyplot as plt 
# import numpy as np 

# x=np.arange(0,10)
# y=x**2
# plt.xlabel('Shivani')
# plt.ylabel('Simran')
# plt.plot(x,y)
# plt.title("nth graph")
# plt.show()

#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(xpoints)
plt.show()





