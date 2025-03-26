
def Check(num):
        match num:
            case 1:
                return "Sunday"
            
            case 2:
                return "Monday"
            
            case 3:
                return "Tuesday"
            
            case 4:
                return "Wednesday"
            
            case 5:
                return "Thursday"
            
            case 6:
                return "Friday"
            
            case 7:
                return "Saturday"
            
            case _:
                return "Invalid Input"
num=int(input("Enter a number"))
print(Check(num))