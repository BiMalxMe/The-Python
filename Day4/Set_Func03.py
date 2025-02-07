#Note
#direct------------>Can store value to new line too
#something+update-->can store value in existing var only


a={'a','e','i','o','u'}
b={'b','i','m','a','r','t','h',"a"}
c={'b','a','t'}
#Union
# print(a.union(b))
#Difference--Gives value in new set also
# print(b.difference(c))

#Difference update-Gives value in exisiting set 
# new=a.difference_update(b)#cant do it
# print(new)#none
#but
# a.difference_update(b)
# print(a)



#Intersection
# print(b.intersection(c))




#Intersection update
# new=b.intersection_update(c)#cant do it if we store value in new var
# print(new)
#BUt
# b.intersection_update(c)#cant do it if we store value in new var
# print()




#symmetric Difference
# num=a.symmetric_difference(c)
# print(num)
#--remove all comman values from the union of a and c

#symmetric diffference update
a.symmetric_difference_update(c)
print(a)




