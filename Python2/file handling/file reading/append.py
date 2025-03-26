# str="Hi my name is bimal chalise and i am lazy"
# f=open("append.txt","w")
# f.write(str)
# f.close()   only adds one tine

#append
str="Hi my name is bimal chalise and i am lazy\n"
f=open("append.txt","b")
f.write(str)
f.close()   # adds multiple times

