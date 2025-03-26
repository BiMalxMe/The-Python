from functools import reduce
#Example of Map Function

mynum=[1,2,3,4,5,6,7,8,9,1]
# sqaredlist=lambda  i:i*i
# mylist=map(sqaredlist,mynum)
# print(list(mylist))

# Filter function
# def even(num):
#     if(num%2==0):
#         return True
#     return False
# a=filter(even,mynum)
# print(list(a))


#Reduce function

#It does sequential computation
'''
If we give a list as a input
1 2 3 4 5 
 3  3 4  5           It adds the first and second element contunuously 
   6  4  5             and add the outcome to the third variable
     10  5
       15


'''
def sum(num1,num2):
    return num1+num2
a=reduce(sum,mynum)
print(a)

b=lambda x,y:x*y
print(reduce(b,mynum))

