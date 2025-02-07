A=['Ross',"Rachel",'Monica','Joe']

#WAP TO SWAP FIRST AND FORTH ELEMENT
A[0],A[3]=A[3],A[0]
print(A)

#WAP TO ADD A NEW VALUE AT SECOND POSITION
A.insert(1,'Roshni')
print(A)

#WAP TO DELETE A VALUE FROM 3RD POSITON
A.remove(A[2])   #or we can write .pop(2)
print(A)

B=[13,7,12,10]

#WAP TO MULTIPLY ALL THE NUMBERS IN THE LIST
mul=1
for i in B:
    mul=mul*i
print(mul)

#WAP TP GET LARGEST NUMBER FROM THE LIST
print(max(B))

#WAP TO GET SMALLEST NUMBER FROM THE LIST
print(min(B))