#1.Write a program to get fibonacci series upto 10 term
#0..1...1...2...3...5....
# a=0
# b=1
# print(a,end=',')
# print(b,end=',')
# for _ in range(2,10):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=',')



#2.Check wheather the number is Prime or not
# num=int(input("Enter any One number\n>"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print("It's prime number")
# else:
#     print("It is not a prime number")





#To chcek wheather a number is palindrome or not
num=int(input("Enter A number\n>"))
rev=0
temp=num
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10

if(temp==rev):
    print("It is a Palindrome ")
else:
    print("It is not a Palindrome")
