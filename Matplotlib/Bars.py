import matplotlib.pyplot as plt
import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x,y)
# plt.show()

# #Giving color to the bar
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.bar(x,y,color='hotpink')

# plt.show()


#in case of horizontal bars

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
# plt.barh(x,y,color='#4CAF50')

# plt.show()


#Note Default height and width of bars is 0.8
#width and height of a  bar
#barh()===>uses height
#bar()===>uses width

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.subplot(1,2,1)
plt.bar(x,y,color='#4CAF50',width=0.5)
plt.subplot(1,2,2)
plt.barh(x,y,color='hotpink',height=0.3)
plt.xlabel('Hi')#giving label just for fun
plt.ylabel('Hlo')

plt.show()