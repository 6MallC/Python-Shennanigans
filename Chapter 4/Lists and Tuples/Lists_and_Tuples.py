list = [1,2,3,'a','b','c']
#mutable
tuple = (11,22,33,'x','y','z')
#immutable- you get a TypeError otherwise
#the way the book did it (noteworthy of being saved)
try:
    tuple[0]= 12
except TypeError as e:
    print(f"an error occured: {e}")

list.append('apples')
list.append('mangos')
list.remove('mangos')
print(list)
