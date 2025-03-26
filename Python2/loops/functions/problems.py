# #Celcius to fahrenheit F = (9/5 × °C) + 32
# temp=int(input("Enter the temperature in celcius"))
# def ftn(value):
#     return (9/5)*value+32
# print(f"The temperature in fahrenheit is {ftn(temp)}")
    

# #gretaer among three using function
# num1=int(input("Enter a first number"))
# num2=int(input("Enter a second number"))
# num3=int(input("Enter a third number"))
# def greater(a,b,c):
            
#         if(a>b and a>c):
#             print("The greater is ",a)
#         elif(b>c and b>num1):
#             print("The greater is ",b)
#         elif(c>num2 and c>a):
#             print("The greater is ",c)
#         else:
#             print("They are equal")
# greater(num1,num2,num3)




'''
***
**
*
'''
# n=int(input("Enter any one number: "))
# def my_fun(num):
#     if(num==0 or num<0):
#         return
#     print("*"*num)
#     return my_fun(num-1)

# my_fun(n)


# # Removing a word from a list using functions
# l=["hari","ram","govinda","archie","an"]
# def rem(l,word):
#     for item in l:
#         l.remove(word)
#         return l
# a=rem(l,"archie")
# print(a)


#Strip function
l=["hari","reema","ramesh"]
def rem(l,word):
    a=[]
    for items in l:
        if items!=word:
            a.append(items.strip(word))
    return a
         

print(rem(l,"har"))