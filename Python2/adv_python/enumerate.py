l=[3,5,73,323,30,22,12]
# index=0
# for item in l:
#     index+=1
#     print("The number in index {} is {}".format(index,item))


#Beside writing that long code we can use enumerate
for index,items in enumerate(l):
     print("The number in index {} is {}".format(index,items))