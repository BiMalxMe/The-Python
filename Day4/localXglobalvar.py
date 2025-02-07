# num=29#it is outside of block so for now its global var
# print(num)
# def hi():
#     num=99#Inside of block so local var
#     return num
# print(hi())#prints val of local var
# print(num)#once def block is terminated first
#           #declared num value is printed as num

# for making num value inside a certain block 
# we can write

num=29
print(num)
def hi():
    global num#value of num becomes global inside 
                #and outside of block
    num=99
    return num
print(hi())
print(num)