# class Employee:
#     a=1
#     def show(self):
#         print(f"The value is {self.a}")##it will print 8
# run=Employee()
# run=Employee()
# run.a=8#it is a instance attribute which will overwrite the value of a in class
# run.show()



#So to acess the class attribute eventhough there is instance attribute by doing this

class Employee:
    a=1
    @classmethod
    def show(self):
        print(f"The value is {self.a}")#it will print 1
run=Employee()
run.a=8#it is a instance attribute which will overwrite the value of a in class
run.show()