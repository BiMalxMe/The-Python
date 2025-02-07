import numpy as np

# #incase of single array elements
# a=np.array([55,33,77,35])
# print(a[0:])
# print(a[0:3])
# print(a[0])
# print(a[::1])


#incase of nested arrays
a=np.array([[55,33,66,22],[34,11,76,39]])
print(a[0:2,0:3]) #if unequal number of element in an array are printed then automaticallty 
#  makes it equal 