import matplotlib.pyplot as plt
import numpy as np

# x=np.array(["A","B","C","D"])
# y1=np.array([1,10,10,1])
# y2=np.array([10,40,90,100])
# y3=np.array([1,10,10,1])

# plt.bar(x,y1,color="teal",width=0.5)
# plt.bar(x,y2,color="brown",bottom=y1,width=0.5)  
# plt.bar(x,y3,color="cyan",width=0.5)
# plt.ylim(0,150)
# plt.show()

# bar chart----


# x=["A","B","C","D"]
# y=[85,67,70,82]
# z=[35,55,65,45]
# w=[1,10,11,69]
# width=0.1
# p=np.arange(len(x))
# p1=[j+width for j in p]
# p2=[j+width for j in p1]
# plt.xlabel("CHARS", fontsize=10)
# plt.ylabel("VALUES",fontsize=10)
# plt.title("BAR CHART",fontsize=10)
# # c=["teal","cyan","teal","cyan"]
# plt.bar(p,y,width,color="teal",alpha=0.5,label="bar")
# plt.bar(p1,z,width,color="g",alpha=0.5,label="bar")
# plt.bar(p2,w,width,color="y",alpha=0.5,label="bar")
# plt.xticks(p+width/2,x)
# plt.legend()
# plt.show()

# x=["MEAT","BANANAS","AVOCADOS","SWEET POTATOES","SPINACH","WATERMELON","COCO WATER","BEANS","LEGUMES","TOMATOES"]
# calories=[250,130,140,120,20,20,10,50,14,19]
# potassium=[40,55,20,30,40,32,10,26,25,20]
# fat=[8,5,3,6,1,1.5,0,2,1.5,2.5]
# width=0.5
# plt.figure(figsize=(9,7))
# p=np.arange(len(x))
# p1=[j+width for j in p]
# p2=[j+width for j in p1]
# plt.xlabel="food"
# plt.ylabel="nutrients"
# plt.title="food vs nutrients"
# plt.bar(p,calories,width,color="b",alpha=0.6,label=calories)
# plt.bar(p1,potassium,width,color="y",alpha=0.6,label=potassium)
# plt.bar(p2,fat,width,color="g",alpha=0.6,label=fat)
# plt.xticks(p+width+width/2,x,rotation=15)
# plt.legend()
# plt.show()


# x=["MEAT","BANANAS","AVOCADOS","SWEET POTATOES","SPINACH","WATERMELON","COCO WATER","BEANS","LEGUMES","TOMATOES"]
# calories=[250,130,140,120,20,20,10,50,14,19]
# potassium=[40,55,20,30,40,32,10,26,25,20]
# fat=[8,5,3,6,1,1.5,0,2,1.5,2.5]
# width=0.5
# plt.figure(figsize=(9,7))
# p=np.arange(len(x))
# p1=[j+width for j in p]
# p2=[j+width for j in p1]
# plt.xlabel="food"
# plt.ylabel="nutrients"
# plt.title="food vs nutrients"
# plt.bar(p,calories,width,color="b",alpha=0.6,label=calories)
# plt.bar(p1,potassium,width,color="y",alpha=0.6,label=potassium)
# plt.bar(p2,fat,width,color="g",alpha=0.6,label=fat)
# plt.xticks(p+width+width/2,x,rotation=15)
# plt.legend()
# plt.show()






import matplotlib.pyplot as plt
import numpy as np

# Data
x = ["MEAT", "BANANAS", "AVOCADOS", "SWEET POTATOES", "SPINACH", "WATERMELON", "COCO WATER", "BEANS", "LEGUMES", "TOMATOES"]
calories = [250, 130, 140, 120, 20, 20, 10, 50, 14, 19]
potassium = [40, 55, 20, 30, 40, 32, 10, 26, 25, 20]
fat = [8, 5, 3, 6, 1, 1.5, 0, 2, 1.5, 2.5]

# Bar width
width = 0.2  # Reduce the width to fit three bars within each category

# Plot size
plt.figure(figsize=(10,5))

# Bar positions
p = np.arange(len(x))
p1 = [j + width for j in p]
p2 = [j + 2*width for j in p]

# Labels and title
plt.xlabel("Food", fontsize=14)
plt.ylabel("Nutrients", fontsize=14)
plt.title("Food vs Nutrients", fontsize=16)

# Plotting the bars
plt.bar(p, calories, width, color="b", alpha=0.6)
plt.bar(p1, potassium, width, color="y", alpha=0.6)
plt.bar(p2, fat, width, color="g", alpha=0.6)

# Set x-ticks
# plt.xticks(p + width, x, rotation=15)

# Add legend
plt.legend()

# Display the plot
plt.show()
