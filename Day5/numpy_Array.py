import numpy as np

# #without using Numpy
# a=[30,40,50]
# b=[50,40,30]
# c=6
# print(a+b)#Just concatinates but doesnot adds 
# #so we use numpy for mathematical calculations



#using Numpy
a=np.array([30,40,50])
b=np.array([50,40,30])
print(a)
print(a+b)
print(a*7)



#We cant send multiple data type
#if you send then all value wll be converted
#to that unique data type
a=np.array([3,44,25,'33'])

print(a)#all converted to string 
