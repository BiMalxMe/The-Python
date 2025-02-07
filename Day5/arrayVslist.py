import numpy as np



#In case of nested array
a=np.array([[44,34,22],[99,55,23]])
print(a)
#In nested array there must be equal element in 
#all nested array else there will be error

#E.g
# eg=np.array([[44,34,22],[99,55,67,23]])

# print(eg)

#Error Occured


#In case of Nested list
b=[[44,34,22],[99,55,23]]
print(b)
#If nested lists have unequal number of element 
#inside  in each list
eg_b=[[44,34,22,66],[99,55,23]]
print(eg_b)#Nothing Happens(No errors)
