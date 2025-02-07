import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# #line color,color=whichcolor
# plt.plot(ypoints,color='r', linestyle = 'dotted')#linestyle can be 'ls' too
# plt.show()

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints,lw = '20.5')#Gives line width,also can weite 'lw'
# plt.show()





#plotting multiple lines
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1,label='This is y1')
plt.plot(y2,label='This is y2')
plt.legend()#to write inside the bar chart

plt.show()