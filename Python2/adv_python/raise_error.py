num1=int(input("Enter any one number: "))
num2=int(input("Enter another number: "))
if(num2==0):
    raise ZeroDivisionError("Sorry this number cant be taken")
else:
    Div=num1/num2
    print (Div)