# #Maximum of three number using function
# def determine(a,b,c):
#     if a>b and a>c:
#         print('Grater is a,',a)
#     elif b>c and b>a:
#         print('Greater is b,',b)
#     else:
#         print('Greater is c,',c)
# determine(15,33,9)


#To create and print a list where the values are
#square of numbers between 1 and 30
# sq_list=[]
# def square(n):
#     for i in range(1,n):
#         sq_list.append(i**2)

# square(30)
# print(sq_list)




#takes a number as a parameter and check if 
#the number is prime or not

# def check(n):
#     count=0
#     for i in range(2,n+1):
#         if n%i==0:
#             count+=1
#     return count
# count=check(83)
# print(count)
# if count>=2:
#     print('The number is not prime')
# else:
#     print('The number is Prime')





#WAPP to sum all number in the list
# sum_list=[44,33,74,90,35,84,14,83,39]
# def sumlist(lis):
#     sum=0
#     for i in lis:
#         sum+=i
#     return sum
# print(sumlist(sum_list))



#fibonacci using recursive function
#0 1 1 2 3 5 8 13 . .. . .
def fb(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fb(n-1)+fb(n-2)
for i in range(10):
    print(fb(i),end=' ')

