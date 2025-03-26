class Shop:
    name="Default"
    company="Microsoft"
    def Info(self):
        print(f"Your name is {self.name}")
    def company1(self):
        print(f"Your company is {self.company} ")
class business(Shop):
    
    def Sal(self):
        super().company1()#call the previous class functions
        super().Info()
        print(f"Your Salaary is incresing from 22 March each year")
call=business()
call.Sal()