import matplotlib.pyplot as plt
import numpy as np

#TO show grindline all over
x=np.array([1,4,7,10])
y=np.array([100,400,700,1000])

# plt.plot(x,y)
# plt.grid()
# plt.show()




# #To show gridline on x axis
# plt.plot(x,y)
# plt.grid(axis='x')
# plt.show()



#To show gridline on y axis
# plt.plot(x,y)
# plt.grid(axis='y')
# plt.show()


#Additional Configs
plt.plot(x,y)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()