a=["Thor","Ironman",'captain America','Hulk']
print(len(a))
print(a.count('Hulk'))
print(a.append('Deadpool'))
#once deadpool is added is list hereis the value
print(a)


#adding value in specific position
a.insert(1,'vision')
print(a)


#To remove value from the list
a.remove('Hulk')
print(a)

#To remove value from certain positon
a.pop(0)
print(a)