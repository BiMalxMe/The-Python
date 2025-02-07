a='Nokia','Samsung','Apple','Lenevo'
print(a)
#as tuple is immutable so conveting it into list
#           to mutate the datas
#converting into list
a=list(a)
print(a)
a.append('Nothing')
print(a)

#After adding conveting this list into tuple again
a=tuple(a)
print('Ater conversion',a)