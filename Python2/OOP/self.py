class Employee_name:
    Name="Krosos"
    age=19

    def fn(self):#instance  needs self keyword to oprate with claass attributes 
        print(f"Hello the age is {self.age} and Name is {self.Name}")

new=Employee_name()
new.fn()#it returns as Emplyee_name.fn(harry) where harry is sent as paramerter but it consisited nothing

#If we rub function without writing self then 'new' named variable is taken as a prameter 
# which disrupts the progeam so by writhinf the self statement the program takes that new named 
# satatement as a class to perform ahead task

