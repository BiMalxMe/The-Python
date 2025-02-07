a={'a','e','i','o','u'}
b={'b','i','m','a','r','t','h',"a"}
c={'b','a','t'}
#isdisjoint
print(a.isdisjoint(b))
#issubset
print(c.issubset(b))#is c subset of b
#issuperset
print(b.issuperset(c))
#update--adds whole set to another set
a.update(c)
print(a)
#clear
a.clear()
print(a)