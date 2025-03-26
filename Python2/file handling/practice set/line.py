#program for getting the strings line number from the exisiting file

with open("line.txt","r") as f:
    lines=f.readlines()
    line01=1
    for line in lines:
        if("python" in line):
            print(f"python is contained, Line no is {line01}")
            break
        line01+=1
    else:
        print("Python is not contained")
    
