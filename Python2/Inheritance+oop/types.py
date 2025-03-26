

# # Python program to demonstrate
# # multiple inheritance
 
# # Base class1
# class Mother:
#     mothername = ""
 
#     def mother(self):
#         print(self.mothername)
 
# # Base class2
 
 
# class Father:
#     fathername = ""
 
#     def father(self):
#         print(self.fathername,end="")
 
# # Derived class
 
 
# class Son(Mother,Father):
#     def parents(self):
#         print("Father :", self.fathername)
#         print("Mother :", self.mothername)
 
 
# # Driver's code
# s1 = Son()
# s1.fathername = "RAM"
# s1.mothername = "SITA"
# s1.parents() # type: ignore
# s1.father()
# s1.mother()



#Multiple Inheritance
# class Grand_father:
#      @staticmethod
#     def greet():
#         print("Hi I am Grandfather")
# class father(Grand_father):
#     @staticmethod
#     def greet():
#         print("Hi I am Father")
# class mother(father):
#      @staticmethod
#     def greet():
#         print("Hi I am Mother")
# class parents(mother):
#     @staticmethod
#     def greets():
#         print("Hi we are parents")
# class child(parents):
    # @staticmethod
#     def greet():
#         print("Hi we are childs")
# a=child()
# a.greet()
class GrandFather:
    @staticmethod
    def greet():
        print("Hi I am Grandfather")

class Father(GrandFather):
    @staticmethod
    def greet():
        print("Hi I am Father")

class Mother(Father):
    @staticmethod
    def greet():
        print("Hi I am Mother")

class Parents(Mother):
    @staticmethod
    def greet():
        print("Hi we are parents")

class Child(Parents):
    @staticmethod
    def greet():
        print("Hi we are children")
