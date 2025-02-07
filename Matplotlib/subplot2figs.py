import matplotlib.pyplot as plt
import numpy as np



#using subplot function
# plt.subplot(1, 2, 1)
# #the figure has 1 row, 2 columns, and this plot is the first plot.
#NOte:subplot must be used before plot



x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1,2,1)
plt.plot(x,y,'o:r')



a = np.array([5, 4, 3, 2])
b = np.array([1, 8, 7, 5])
plt.subplot(1,2,2)
plt.plot(a,b,'o:b')
plt.show()