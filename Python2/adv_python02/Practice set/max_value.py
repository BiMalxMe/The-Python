#Program for finding out the maximum numbers among the enteres numbers in list

from functools import reduce
mylist=[3,4,5,89,759,43,222,334,567,222,566]
def func(a,b):
    if(a>b):
        return a
    return b
a=reduce(func,mylist)
print(a)