#Tuples can be converted to lists and vice versa

#exercise
tuple1 = (1,2,3)
tuple2 = (1,2,3)
tuple0 = tuple1 + tuple2
print ("conceated tuple:", tuple0)
index = tuple0.index(2)
print(index)
nested = (1,2,(3,4)) # nested counts as one entry
print(nested[2])
