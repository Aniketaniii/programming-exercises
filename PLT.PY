import matplotlib.pyplot as plt
import numpy as np

plt.title("SALES",color="brown",font="ariel",fontsize=20)
plt.xlabel("MONTH",color="black",font="ariel",fontsize=20)
plt.ylabel("NUMBER OF BICYCLE SOLD ",color="black",font="ariel",fontsize=20)

x=np.array(["JAN","FEB","MAR","APR","MAY","JUN"])
y=np.array([50,30,40,30,20,50])

plt.plot(x,y,marker='o'
         ,markerfacecolor="yellow"
         ,markeredgecolor="red"
         ,markersize=7
         ,linewidth=2
         ,color="green"
         ,linestyle="solid"
         )
plt.show()