#copying one files data to another file

with open("copy.txt","r") as f:
    read=f.read()
with open("copy1.txt","w") as f:
    f.write(read)
    