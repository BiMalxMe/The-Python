#WAP TO FIND MAX AND MIN IN THE SET
# num={1,4,2,6,3,9,6,3,1}
# print(max(num))
# print(min(num))

#TO FIND COMMON ELEMENT IN THREE SET LIST USING SET
# l1=[1,2,3,4,5]
# l2=[4,5,6,7,8]
# l3=[1,4,9]
# l1=set(l1)
# l2=set(l2)
# l3=set(l3)
# print(l1.intersection(l2,l3))


#WAP TO FIND DIFFERENCE BETWEEN TWO SET

num1={1,4,2,6,3,9,6,3,1}
num2={5,1,10,11,66,6}
num3={1,6,3}
# print(num1.difference(num2))


#WAPP TO REMOVE AN ITEM FROM THE SET
num1.discard(22)
print(num1)


#TO CHECK IF A SET IS SUBSET OF ANOTHER SET
print(num3.issubset(num1))