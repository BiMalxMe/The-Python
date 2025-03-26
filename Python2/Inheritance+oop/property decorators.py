# #Trying By Myself

# class Fruits:
#     def __init__(self,name:str):
#         self._name=name
#     @property
#     def show(self):
#         print(f"The fruit you entered is {self._name}")
#         return self._name
#     @show.setter
#     def show(self,value):
#         self._name=value
#         print(f"The fruit is now {self._name} ")

#     @show.deleter
#     def show(self):
#         print(f"{self._name} is now deleted")
#         del self._name
# a=Fruits('Banana')
# print(a.show)
# a.show='Orange'
# del a.show
# print(a.show)






# #according to code with harry


# class Employee:
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
#     @name.setter
#     def name(self,value):
#         self.fname = value.split("  ")[0]
#         self.lname = value.split("  ")[1]
#         print(f"The value is {self.name}")
# e=Employee()
# e.name="Haarry  Ram af"
# print(e.name)





#USING PROPERTRY DECORATOR METHOS 









