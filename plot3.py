import  matplotlib.pyplot as plt
import numpy as np 
x=np.arange(0,10,2)
y=x**2
z=x**3
plt.xlabel("number")
plt.ylabel("square of number")
plt.plot(x,y,marker="*",mec="b",mfc="beige",ms="10",lw="1",c="k")
plt.plot(x,z,marker="o",mec="b",mfc="y",ms="10",lw="1",c="b")
plt.show()
