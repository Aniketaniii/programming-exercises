import matplotlib.pyplot as plt
import numpy as np

# population=[200,400,500,700,100]
# countries=['A','B','C','D','E']
# plt.title("population",fontsize=30,color="red")
# plt.xlabel("countries")
# plt.ylabel("population")
# plt.bar(countries,population
#         ,color="orange"
#         ,width=.5)
# plt.show()



fruits=["MANGO","APPLE","BANANA","PAPAYA","GUVA"]
sales=np.array([50,30,20,80,60])
color=["GOLD","RED","YELLOW","orange","green"]
plt.pie(sales,labels=fruits,
         autopct='%1.1f%%',
         colors=color,
         explode=[0.2,0.3,0.1,0.02,.5],
         shadow=True)
plt.show()
