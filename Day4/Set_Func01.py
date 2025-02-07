a={"spiderman","batman",'superman','vision'}

#add
a.add('Ironman')
print(a)

#pop
a.pop()#==>Pops random valuw
print(a)

#remove-It shows valuw error
a.remove('superman')
print(a)

#discard-it doesnot throws valueerroe when item is missing
a.discard('superman')
print(a)

#Copy
b=a.copy()
print(b)