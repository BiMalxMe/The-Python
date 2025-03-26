#Increment salalry using class attribute
class Employee:
    salary=700001
    increment=30
    def __init__(self):
        self.Current_salary=Employee.salary
    def incremented_salary(self):
        incremented_salary=(Employee.increment*self.Current_salary)/100
        self.Current_salary += incremented_salary
        return self.Current_salary
    
    def show_salary(self):
        print(f"Current salary: {self.Current_salary}")
e=Employee()
e.incremented_salary()
e.show_salary()
