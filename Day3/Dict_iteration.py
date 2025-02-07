students={
    "name":'John',
    'class':4,
    'roll no':21
}
print(len(students))

#printing the keys from the dictionary
for i in students:
    print(i)
for i in students.keys():
    print(i)


#printing only the values from the dictionary
for i in students:
    print(students[i])

#or
for i in students.values():
    print(i)



#To Print both values and keys
for i,j in students.items():
    print(i,':',j)