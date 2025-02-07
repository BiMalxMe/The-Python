import matplotlib.pyplot as plt
import numpy as np

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x,y,color='hotpink')#Can give different colors


# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y,color='cyan')
# plt.show()




#coloring each dot

# x = np.array([5,7,8,7,6])
# y = np.array([99,86,87,57,86])
# colors = np.array(["red","green","blue","orange","black"])

# plt.scatter(x, y, c=colors)

# plt.show()


# #giving size to each element
# x = np.array([5,7,8,7,6])
# y = np.array([99,86,87,57,86])
# sizes = np.array([199,1086,870,57,2000])
# colors = np.array(["red","green","blue","orange","black"])

# plt.scatter(x, y,c=colors,s=sizes)

# plt.show()



#giving alpha(ttransparency) to each element
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.show()

