dict1= {'x':'1','y':'2','z':'purple','a':'alpha','b':'beta'}
print(len(dict1))
for key in dict1.keys():
    print(key)
items = dict1.items() #lists all items 
#exercise
dict1['c']= 'me'
print(dict1)
dict1['z']= 'zeta'
del dict1['x']
# we also have get and pop

