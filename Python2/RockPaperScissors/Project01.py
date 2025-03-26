#Making a rock paper scissors game
'''
rock:0
paper:1
scissors:2

'''
import random
computer=1
print(
        
'''
For Rock: Enter r
For Paper: Enter p
For Scissors: Enter s
    '''
        
)

Yournum=input("Enter your choice")
youdict={
    "r":0,
   "p": 1,
    "s":2
}
revdict={
     0:"r",
     1:"p",
     2:"s"
}
print("computer choice is ",revdict[computer])
you=youdict[Yournum]
if(you==computer):
        print("It is a draw")
else:
        if(you==0 and computer==1 ):
                print("Computer Wins")
        elif(you==0 and computer==2 ):
                print("You Win")
        elif(you==1 and computer==0 ):
                print("You Win")
        elif(you==1 and computer==2 ):
                print("Computer Wins")
        elif(you==2 and computer==0 ):
                print("computer Win")
        elif(you==2 and computer==1 ):
                print("you Wins")
        else:
                print("something went wrong")