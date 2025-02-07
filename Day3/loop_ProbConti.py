print('Area Calculator'.center(28,'_'))
while  True:
    print('''
          1---> Area of Reactangle
          2---> Area of Square
          3---> Area of Triangle
          ''')
    choose=int(input('Enter any Number from 1 to 3\n>'))
    if choose>=1 and choose<=3:

                if choose==1:
                    while True:
                        length=int(input("Enter the length of the rectangle\n>"))
                        breadth=int(input("Enter the breadth of the ractangle\n>"))
                        print('Area of Rectangle : {}'.format(length*breadth))
                        choice=input("Do you to Find Rectangles Area Again(y/n)")
                        if choice=='n':
                            break

                if choose==2:
                    while True:
                        length=int(input("Enter the Length of side of a square\n>"))
                        print('Area of square: {}'.format(length*length))
                        choice=input("Do you to Find Square's Area Again(y/n)")
                        if choice=='n':
                            break
                if choose==3:
                    while True:
                        base=int(input("Enter the Base of Triangle\n?"))
                        height=int(input("Enter the Height of Triangle\n>"))
                        print('Area of Triangle : {}'.format((base*height)/2))
                        choice=input("Do you to Find Triangle's Area Again(y/n)")
                        if choice=='n':
                            break
    else:
        print("Invalid Input")

    choice1=input("Do you to Find Areas Again (y/n)")
    if choice1=='n':
        break
