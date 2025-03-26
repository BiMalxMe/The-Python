from random import randint
class Bus:
    def __init__(self,fro,to,trainNo):
        self.fro=fro
        self.to=to
        self.trainNo=trainNo
    print("Displaying The results")
    def book(self):
        print(f"Train no {self.trainNo} is available to go {self.fro} to {self.to}") 
    def getStatus(self): 
        print(f"Train no{self.trainNo} is scheduled at 8 Am") 

    def Price(self): 
        print(f"Train no{self.trainNo} going {self.fro} to {self.to} costs total pay sum of Rs{randint(500,3000)}")
a=int(input("Enter Train No you want to travel:")) 
b=input("Enter your railway place:") 
c=input("Enter Where you want to go:")
call=Bus(b,c,a)
call.book()
call.getStatus()
call.Price()
