students={
    'Name':"Bimal",
    'Age':22,
    'Roll no':98
}

#get
print(students.get('Name'))#gets vals
#item
a=students.items()
print(a)#Prints in the form of tuples

#keys
print(students.keys())

#values
print(students.values())

#copy
d=students.copy()
print(d)