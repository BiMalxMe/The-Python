#as called as init and dunder method
class cname:
    def  __init__(self,Name,Age,Salary):
        self.Names=Name
        self.Ages=Age
        self.Salarys=Salary 

    print("Displaying the values")
    def display(self):
          print(f"Name: {self.Names}, Age: {self.Ages}, Salary: {self.Salarys}")

a=cname("Ramesh",54,1200000)
b=cname("Mukesh",44,5467700)
c=cname("Rajesh",51,6700400)
d=cname("Ramish",24,870000)
e=cname("Jamesh",36,1770000)
f=cname("Jigesh",21,88000)
g=cname("haresh",44,100000)
a.display()
b.display()
c.display()
d.display()
e.display()
f.display()
g.display()
