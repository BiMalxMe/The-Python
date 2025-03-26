#Create such a progrma where info about programmers is stored in  a class
class Programmer:
    Company="Microsoft"
    def __init__(self,Name,Salary,Post):
        self.Name=Name
        self.Salary=Salary
        self.Post=Post
        print("This is a Basic Information")
        print(f"Name is {self.Name}\nSalary is {self.Salary}\nPost is {self.Post}")
Programmer("Kristi",5,"Head Chef")
Programmer("Krishmas",50000000,"Head sir")
Programmer("Sameer",5000,"Dancer")
Programmer("Biplove",50000,"Teacher")
Programmer("Darshan",0,"salesman")

