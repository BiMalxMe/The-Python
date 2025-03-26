#Multiplication table of any number

# num=int(input("Enter number you want to get multiplication table"))
# for i in range(0,11):
#     ans=num*i
#     print(f"{num}*{i}={ans}")


#printing only the name starting with g and greeting them
# list=['Gouti',"shrawan","binnet","Ganesh","gopi"]
# for name in list:
#     if(name.startswith('G')):
#         print(f"Hello {name}")

#Multiplication table using while loop

# num=int(input("Enter the number bruh"))
# i=0
# while(i<11):
    # print(f"{num}*{i}=={num*i}")
#     i+=1

#Checking wheather  a given number is prime or not

# num=int(input("Enter the number bruh"))
# for i in range(2,num):
#     if(num%i)==0:
#         print("It is not a prime")    
        
# else: 
#      print("It is  prime")


#sum of n natural number

# num=int(input("Enter the number bruh"))
# i=1
# sum=0
# while(i<=num):
#     sum+=i
#     i+=1

# print(sum)

#factorial using for loop

# num=int(input("Enter the number bruh"))
# fact=1
# for i in range(1,num+1):
    
#         fact=fact*i
        
# print(fact)

'''
  *   print this
 ***
*****
# '''
# num=int(input("Enter the number bruh"))
# for i in range(1,num+1):
#     print(" "*(num-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")

''' 
* * *
*   *
* * *

'''

# num=int(input("Enter the number bruh"))
# for i in range(1,num+1):
#     if(i==1 or i==num):
#         print("*"*num)
#     else:
#         print("*",end="")
#         print(" "*(num-2),end="")
#         print("*",end="")
#         print("")
# Explanation
'''
Explanation for num = 3:
User Input:

When num = 3, the user enters 3 as the input.
Outer Loop (for i in range(1, num + 1):):

This loop iterates through each row from 1 to 3.
Conditions Check (if i == 1 or i == num:):

For i = 1 and i = 3, the condition if i == 1 or i == num: is true.
Printing for i = 1:

In the first iteration (i = 1):
The condition if i == 1 or i == num: is true (i == 1).
Therefore, it prints "*" repeated num times ("*" * num).
Output: "***" (a line of three asterisks).
Printing for i = 2:

In the second iteration (i = 2):
The condition if i == 1 or i == num: is false (i != 1 and i != num).
Therefore, it prints:
"*": One asterisk at the beginning.
" " * (num - 2): Two spaces in between (" ").
"*": One asterisk at the end.
Output: "* *" (a line with an asterisk at the beginning and end, with two spaces in between).
Printing for i = 3:

In the third iteration (i = 3):
The condition if i == 1 or i == num: is true (i == num).
Therefore, it prints "*" repeated num times ("*" * num).
Output: "***" (a line of three asterisks, similar to the first row).


'''


# #Multiplication table in reverse using for loop
# num=int(input("Enter the number bruh"))
# for i in range(1,11):
#     print(f"{num}*{11-i}=={num*i}")

a=0.1
b=0.2
print(float(a+b))
