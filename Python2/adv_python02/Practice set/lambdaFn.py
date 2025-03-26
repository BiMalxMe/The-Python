#program using filter command to print inly the number divisible by 5

newlist=[1,34,55,50,99,45,32,10]
a=filter(lambda i:i%5==0,newlist)
print(list(a))