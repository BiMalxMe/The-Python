marks={
    "harry":55,
    "bimal":100,
    "rohan":77

}
print(type(marks))
print(marks["bimal"])#used to print the marks of bimal
marks['harry']=58  #update the marks of value from 55 to 58
marks.update({"rohan":89})
print(marks)
marks["sameer"]=90#adds new value in the existing dictionary 
print(marks)
del marks['rohan']
print(marks)#deletes the value in a dictionary
for key in marks:
    print(key,'is',marks[key])#sets the format of given dictionary 
# marks.clear()
# print(marks)#for cleering the of a dictionary
print(marks.keys())
print(marks.values()) 
new=marks.get('bimal')
print(new)