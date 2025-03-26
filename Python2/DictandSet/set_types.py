a={1,22,64,32}
print(type(a))
b={56,541,78,32}
c={22}
print(a.union(b))
print(a.intersection(b))
print(a-b)
# # Set comprehension
# squares = {x+1 for x in range(11)}
# print(squares)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81} Extra ho yo sabai#
subset_check=c.issubset(a)#checks wheather a given set is a subset or not
print(subset_check)
