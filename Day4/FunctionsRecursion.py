# def func():
#     print('Subtracting the values')
# func()

# £Recursion

#Goes to infinite loop until python itself cancels it
# def hello():
#     print('kristi')
#     return hello()
# hello()

#factorial by recursion

n=int(input('Enter number : '))
def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
print(fact(n))