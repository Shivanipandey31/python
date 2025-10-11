import matplotlib.pyplot as plt 
import numpy as np 

cse=["Shivani","Simran","shalini","Srishti","Shreya"]
meawww=[50,30,50,30,50]
plt.pie(meawww,labels=cse,startangle=90,explode=[0,0.6,0,0.6,0],shadow=True,colors=["teal","g","teal","g","teal"])
plt.legend(title="toppers")
plt.show()