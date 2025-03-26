class Shop:
    name="Default"
    company="Microsoft"
    def Info(self):
        print(f"Your name is {self.name}")
    def company1(self):
        print(f"Your company is {self.company} ")

class business(Shop): #ITs ingeritance class which includes all the attributes of Shop class
      
    def Sal(self):
        print(f"Your Salaary is incresing from 22 March each year")
a=business()
a.Info()
a.company1()
a.Sal()

