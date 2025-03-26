num=int(input("Enter any one number"))
lis=[i*num for i in range(0,11)]
print(lis)
with open("mul.txt","a") as f:
    f.write(str(lis)+'\n')
