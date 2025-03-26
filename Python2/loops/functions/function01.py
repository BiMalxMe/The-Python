
# def sum():#Function declaration
#     num1=int(input("Enter any one number"))
#     num2=int(input("Enter any one number"))
#     print(num1+num2)
# sum()#Function call
# print("Thanks")
# sum()#Function call
# print("Thanks")
# sum()#Function call
# print("Thanks")
# sum()#Function call
# print("Thanks")

# #Greeting the user for having a good day

# def greet(name):
#     print("have a good day "+name)
# greet("gopi")


# #functions with parameter
# def greet(name,ending):
#     print("have a good day"+name)
#     print(ending)
# greet("gopi"," Thank you")


# #Functions with a return value

# def add_numbers(a, b):
#     # Function to add two numbers and return the result
#     return a + b

# # Call the function and store the returned result
# result = add_numbers(3, 115)
# print("Result of adding 3 and 115:", result)  # Output: Result of adding 3 and 5: 8


# #Default value in function
# def myfunction(name,ending="Thanks Bruhh"):
#     print(f"Hello {name}")
#     print(ending)#if we dont give value of ending it automatically prints the default one
# myfunction("Gopi")

# #Just practicing harsh method is used
# import math

# def print_circle(radius):
#     # Determine the center of the circle
#     center = (radius, radius)
    
#     # Iterate through each point in a square bounding the circle
#     for y in range(2 * radius + 1):
#         for x in range(2 * radius + 1):
#             # Calculate distance from center to current point
#             distance = math.sqrt((x - center[0])**2 + (y - center[1])**2)
            
#             # If distance is approximately equal to radius, print asterisk, else print space
#             if abs(distance - radius) < 0.5:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print()  # Move to the next line after each row of the circle

# # Example usage:
# radius = 10
# print_circle(radius)



