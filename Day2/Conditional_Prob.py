#Check positive or Negative 
# num=int(input("Enter a number to check"))
# print("Its Positive") if num>0 else print("It's Smaller")

#Odd or Even
# num=int(input("Enter a number to check"))
# print("It's Even") if num%2==0 else print("It's Odd")


#check Vowel or not
# vowel=["a","e","i","o","u"]
# letter=input("Enter a letter to check")
# if letter  in vowel:
#     print("Its Vowel")
# else:
#     print("it's Consonent")






#Sum of all even numbers upto 50
# sum=0
# for i in range(1,51):
#     if i%2==0:
#         print("adding",i)
#         sum+=i
# print("The total sum is ",sum)

#square of 20 numbers
# for i in range(1,21):
#     print(i**2)


#Sum of 10 odd numbers
# num = 0
# sum = 0
# while num <= 20:
#     if num % 2 != 0:
#         sum += num
#     num += 1
# print(sum)


#divisible by 8 and 12 or not
# for i in range(100):
#     if i%8==0 and i%12==0:
#         print(i)








#Making a Billing Counter of a supermarket
while True:
    Amount=0
    Name=input("Enter the name of customer\n>")
   
    while True:
        
        Quatity=int(input("Enter the Total number of goods\n>"))
        Cost=int(input("Enter Total Amount of Goods\n>"))
        Amount+=Quatity*Cost
        choice=input("Would you like to add More items(y/n)\n>")
        if choice=='n':
            break
       
    print(f'''
        Name={Name}
        Amt={Amount}

        ''')
    choice1=    input("Would you like to add new customer or quit(q)")
    if choice1=='q':
     break