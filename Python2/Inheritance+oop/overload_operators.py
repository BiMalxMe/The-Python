# class sum:
#     def __init__(self,num) -> None:
#         self.num=num
#     def __add__(self,num):
#         return self.num+num.num
# n=sum(1000000000)
# m=sum(262562763)
# print(n+m)

# #Doing vector addition
# class Vector:
#     def __init__(self,i,j,k):
#         self.i=i
#         self.j=j
#         self.k=k
#     def __add__(self,another):
#         return Vector(self.i+another.i,self.j+another.j,self.k+another.k)
#     def __str__(self):
#         return (f"The addition of those two vectors are{self.i}i,{self.j}j,{self.k}k")
# a=Vector(1,2,3)
# b=Vector(1,15,3)

# print(a+b)



# #Doing vector addition

# class Vector:
#     def __init__(self,i,j,k):
#         self.i=i
#         self.j=j
#         self.k=k
#     def __sub__(self,another):
#         return Vector(self.i-another.i,self.j-another.j,self.k-another.k)
#     def __str__(self):
#         return (f"The  vectors are{self.i}i,{self.j}j,{self.k}k")
# b=Vector(1,15,3)
# a=Vector(1,2,3)

# print(b)
# print(a)
# print(b-a)





#Doing vector amulyiplication

class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __mul__(self,another):
        return Vector(self.i*another.i,self.j*another.j,self.k*another.k)
    def __str__(self):
        return (f"The  vectors are{self.i}i,{self.j}j,{self.k}k")
b=Vector(1,15,3)
a=Vector(1,2,3)