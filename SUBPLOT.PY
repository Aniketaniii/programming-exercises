import matplotlib.pyplot as plt
import numpy as np

x=([100,200,500,140,260])
y=([5,10,15,20,25])

plt.subplot(1,2,1)
plt.plot(x,y)

x=([200,400,260,511,356])
y=([5,10,15,20,25])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()