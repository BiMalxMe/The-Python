import pandas as pd

# dic={"key":[1,2,3,4],
#      'Name':['wanda','mathew','fraulkner','mcgurk'],
#      "fav_col":['Blue','Green','Purple','Neon'],
#      'Brand':["jokey",'Rolls','Bugatti','Shanel']}
# data=pd.DataFrame(dic)

# pivoted = data.pivot(index="key", columns="Name",values='fav_col')
# print(pivoted)

# #INcase of multiple values
# pivoted2 = data.pivot(index="key", columns="Name",values=['fav_col','Brand'])
# print(pivoted2)




#melt
dic={
     'Name':['wanda','mathew','fraulkner','mcgurk'],
     "fav_col":['Blue','Green','Purple','Neon'],
     'Brand':["HnM",'Rolls','Bugatti','Shanel']}
data=pd.DataFrame(dic)
print(pd.melt(data,id_vars=['Name'],value_vars=['Brand']))

#also we can give name for the variable and value
# for_example
print(pd.melt(data,id_vars=['Name'],value_vars=['Brand'],value_name='Brands_list',var_name='Brand Var'))
#we can see set names in variable and value 