import numpy as np
import random


#Write a NumPy function to create a 3x3 matrix of ones.
# a=np.matrix([[20,11,87],[23,43,55],[47,29,76]])
# print(a)

#addition of array
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# def sum(a,b):
#     return a+b
# print(sum(a,b))

#WAP to compute standard_deviation
# data = np.array([10, 20, 30, 40, 50])
# print(np.std(data))

#Write a function that reshapes a 1D NumPy array
#  of 12 elements into a 3x4 2D array.
# array_1d = np.arange(12)
# print(array_1d.reshape(3, 4))


#Write a function to extract the diagonal elements 
#from a 4x4 NumPy array matrix

# arr = np.matrix([[5, 12, 15, 22],[45,30,35,95]\
#  ,[30, 35, 40 ,45],[20,50,30,65]])
# print(arr)
# print(np.diag(arr))


#Write a function that performs matrix 
# multiplication between two 2x2 NumPy matrices.

# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])

# result = np.dot(A, B)
# print(result)



#Write a function that calculates the dot product of
#  two NumPy arrays a and b where a = np.array([1, 2, 3]) and b = np.array([4, 5, 6]).
# a = np.array([1, 2, 3]) 
# b = np.array([4, 5, 6]) 
# results=np.dot(a,b)
# print(results)



#Write a function that computes the sum of each 
# column in a 3x3 NumPy array.

# a=np.arange(9)
# arr=a.reshape(3,3)
# print(arr)
# print(sum(arr[0]),sum(arr[1]),sum(arr[2]))



#Write a function that filters out all values in a NumPy array 
# arr = np.array([5, 12, 15, 22, 30, 35]) that are greater than 20.
# arr = np.array([5, 12, 15, 22, 30, 35])
# print(arr[arr>20])




#Given a 2D array arr = np.array([[1, 2, 3], [4, 5, 6]]) and a 1D array 
# vec = np.array([10, 20, 30]), write a function that adds the 
# vector to each row of the matrix using broadcasting.

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# vec = np.array([10, 20, 30])
# print(arr+vec)



#Write a function that generates a 5x5 matrix of random numbers between 0 and 1,
#  and then finds the maximum value in each row.
lis=[]
for _ in range(0,25):
    choice=random.randint(0,1)
    lis.append(choice)
arr=np.matrix(lis)
final_mat=arr.reshape(5,5)
print(final_mat)
print('Max at first row',np.max(final_mat[0]))
print('Max at second row',np.max(final_mat[1]))
print('Max at third row',np.max(final_mat[2]))
print('Max at fourth row',np.max(final_mat[3]))
print('Max at fifth row',np.max(final_mat[4]))
print('Min at first row',np.min(final_mat[0]))
print('Min at second row',np.min(final_mat[1]))
print('Min at third row',np.min(final_mat[2]))
print('Min at fourth row',np.min(final_mat[3]))
print('Min at fourth row',np.min(final_mat[4]))
