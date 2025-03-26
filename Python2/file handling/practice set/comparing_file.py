#comparing wheather the contents if file are same or different

with open("copy.txt") as f:
    read=f.read()
with open("copy1.txt") as f:
    read1=f.read()
if(read==read1):
    print("Contents is same")
else:
    print("contents are different")