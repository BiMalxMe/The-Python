#Replacing the preexisting word from the text file 

with open("word.txt","r+") as f:
    read=f.read()
    Rep=read.replace("#####","Love YOu--")
    f.seek(0)
    f.write(Rep)