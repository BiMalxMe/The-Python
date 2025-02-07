import matplotlib.pyplot as plt
import numpy as np


#plot1
x=np.array([22,14,16,8])
y=np.array([10,90,80,40])
plt.subplot(2,3,1)
plt.title('This is 1th plot')
plt.plot(x,y,":b")
#plot2
x=np.array([2,4,6,8])
y=np.array([20,40,60,80])
plt.subplot(2,3,2)
plt.title('This is 2th plot')
plt.plot(x,y,":b")
#plot3
x=np.array([1,2,3,4])
y=np.array([20,40,80,10])
plt.subplot(2,3,3)
plt.title('This is 3th plot')
plt.plot(x,y,":b")
#plot4
x=np.array([1,3,5,7])
y=np.array([10,40,160,88])
plt.subplot(2,3,4)
plt.title('This is 4th plot')
plt.plot(x,y,":b")
#plot5
x=np.array([7,8,9,10])
y=np.array([111,114,101,99])
plt.subplot(2,3,5)
plt.title('This is 5th plot')
plt.plot(x,y,":b")
#plot6
x=np.array([11,13,15,16])
y=np.array([22,28,32,40])
plt.subplot(2,3,6)
plt.plot(x,y,":b")
plt.title('This is 6th plot')
plt.tight_layout(pad=5.0)#==> to give spaces between diffeent plots
plt.suptitle('Plots')
plt.show()

#you can give title to whole plotss ny plt.suptitle()
#you can give differwnt title using plt.title()