#py program to check wheather python string is contained in file or not

with open("log.txt","r") as f:
    read=f.read()
    a=read.readlines("python")
    if("python" in read):
        print("python is contained")
    else:
        print("Python is not contained")
    print(a)