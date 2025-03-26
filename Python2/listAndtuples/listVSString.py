friends= ["bimal","sofia", True, 98.008]
asc=[22,5,6,88,90,11,34,67,62,86]
# The difference betweem a string and list is that we cant
# change the original as it is immutable but in list its possible

# Example of list_method
friends[0]="shyam"
print(friends)
asc.sort()
print(asc)

# Example of string_method
var="Ramesh"
var[0]="j"
print(var) #as a immutable string it cant change a strings content of original
