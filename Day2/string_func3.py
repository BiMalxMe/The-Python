A='Ant Man And The Wasp'

#1 ................startswith(letter)
#for range too .startswith(letter,rangestart,rangeend)

# print(A,A.startswith('A'))


#2 ................endswith(letter)

# print(A,A.endswith('p'))


#2 ................endswith(letter)

# print(A,A.endswith('p'))


#3....................swapcase()===If upper then converts to lower else vice versa
# print(A,A.swapcase())



#4....................strip()===>Used to trim the string
# print(A,A.strip())
# B='    ***   Ant Man'
# print(B,B.strip("*, "))#Removes the * and spaces unnecessary


#5......................split()==> Splits the variable into list
# print(A,A.split(' '))

#6......................ljust()==>shifts towards left
# print(A.ljust(29,'*'),'Hii')

#7......................rjust()==>shifts towards right
# print(A.rjust(29,'*'),'Hii')

#8.......................replace('Existing','New')
# print(A,A.replace('Ant','Hulk'))

#9.......................index()
# print(A.index('Wasp'))

M='bimaligfhgtsrhi'
# print(M.find('i'))#Gives the first found position of i
# print(M.rfind('i'))#Gives the highest found position of i

#difference between find() and index()
print(M.find('n'))#It give -1 as output if it cannot find the character
print(M.index('n'))#It directly gives the valueerror if it doesn't finds the character