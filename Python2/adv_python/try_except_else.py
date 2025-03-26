try:
    print(int(input("Enter any number")))
except ValueError as v:
    print(v)
else:
    print("Your number is inputes sucessfully")
