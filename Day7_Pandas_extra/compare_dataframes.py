import pandas as pd
dat1={'Fruits':['Mango','Orange','Pineapple','Apple'],
       'Price':[100,150,50,200],
       'Quantity':[12,5,4,20]}       
data1=pd.DataFrame(dat1)
print(data1)
data2=data1.copy()

#Applying the change into the exisiting Prices
data2.loc[0,'Price']=120
data2.loc[3,'Price']=300
data2.loc[3,'Quantity']=25
print(data2)


#Incase of Bulk datas
print(data1.compare(data2))
#default axis=1
print(data1.compare(data2,align_axis=0))
print('\n\n')
print(data1.compare(data2,keep_shape=False))
print(data1.compare(data2,keep_shape=True))
#keep_shape=False is always defalut
#==>IT means only changed data will be displayed
#keep_shape=True
#==>It means all the changed and unchanged
#value are displayed
print(data1.compare(data2,keep_shape=True,keep_equal=True))
#keep_equal=Put in the original cacneling all  kinds of change


