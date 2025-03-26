import math
class Calculator:
    def __init__(self,num):
        self.Number=num
        print("These are the values")
        square=self.Number*self.Number

        
        cube=self.Number*self.Number*self.Number
        sqrt=math.sqrt(self.Number)


        print(f"The square {self.Number} is {square} ")
        print(f"The cube {self.Number} is {cube}")
        print(f"The sqrt {self.Number} is {sqrt}")
num=int(input("Enter any one nnumber:"))
Calculator(num)


