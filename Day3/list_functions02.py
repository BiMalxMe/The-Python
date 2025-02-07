a=['Thor','Hulk','spiderman','Ironman','Deadpool']


#to create a copy of the list
b=a.copy()
print(b)


#to acess the element
print(a.index('Hulk'))

#To extend the list
c=['1Superman','2Ahanos']
a.extend(c)
print(a)#Adds value of c in a

#To reverse the list
print(a[::-1])#1
a.reverse()#2
print(a)

#To sort the list
c.sort()
print(c)

#To clear all the data of the list
a.clear()
print(a)