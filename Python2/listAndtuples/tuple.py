a=("ram",44,True,"Hari",889,44)
print(type(a))
#tuple is immutable
#some tuple types
index =a.index("Hari")
print(index)#gives the position of a give value
count=a.count(44)#counts no of given value in a given tuple
print(count)
# tuple(seq): Converts a sequence (e.g., a list) into a tuple.
lst = [1, 2, 3, 4]
tup = tuple(lst)
print(tup)  # Output: (1, 2, 3, 4)
b=set()
print(type(b))

