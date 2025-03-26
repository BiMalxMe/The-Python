# class Name:
#     def __init__(self,Fname,Lname):
#         self.Fname=Fname
#         self.Lname=Lname

#     def email(self):
#         return 'Your eamil is {}.{}@gmail.com'.format(self.Fname,self.Lname)   

#     def Fullname(self):
#         return 'Your full name is {} {}'.format(self.Fname,self.Lname)
    
# a=Name("Harish",'Chapagain')
# a.Fname="manessh"
# print(a.Fname)
# print(a.email())#calling in by email() calls the function
# print(a.Fullname())



#using property decorator

# class Name:
#     def __init__(self,Fname,Lname):
#         self.Fname=Fname
#         self.Lname=Lname
#     @property#using poperty decoratore so email will be an  attribute
#     def email(self):
#         return 'Your eamil is {}.{}@gmail.com'.format(self.Fname,self.Lname)   

#     def Fullname(self):
#         return 'Your full name is {} {}'.format(self.Fname,self.Lname)
    
# a=Name("Harish",'Chapagain')
# a.Fname="manessh"
# print(a.Fname)
# print(a.email)#its mo longer a function so () is not needed, its a attribute
# print(a.Fullname())



#using  setter


class Name:
    def __init__(self,Fname,Lname):
        self.Fname=Fname
        self.Lname=Lname
    @property
    def email(self):
        return 'Your eamil is {}.{}@gmail.com'.format(self.Fname,self.Lname)   
    @property
    def Fullname(self):
        return '{} {}'.format(self.Fname,self.Lname)
    @Fullname.setter
    def Fullname(self,newname):
        fname,lname=newname.split(' ')
        self.Fname=fname
        self.Lname=lname

    
a=Name("Harish",'Chapagain')
a.Fname="manessh"#what if we enter a full name and want values accordingly
a.Fullname='Sankalp Mehta'
print(a.Fname)
print(a.email)
print(a.Fullname)