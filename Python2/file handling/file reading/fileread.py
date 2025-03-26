# st="Hi this is my first file handeling"
f=open("syms.txt","r")
# a=f.readline()
# b=f.readline()
# c=f.readline()
# d=f.readline()
# e=f.readline()
# print(a,b,c,d,e=="",type(a))
# f.close()



#by while loop
read=f.readline()
while(read!=""):
    print(read)
    read=f.readline()
f.close()