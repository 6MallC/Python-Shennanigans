set1 = {'lemon', 'orange', 'lime'}
set2 = {'lemon'}
print('lemon' in set1)
print(set2.issubset(set1)) # boolian to check if all itmes in one set is present in a larger one
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2)) # first not second
print(set1.symmetric_difference(set2)) # first or second
#can use == or != to compare
# union and intersect either add all values together (skipping dupes) or adds all common items together\
#exercise in notes
