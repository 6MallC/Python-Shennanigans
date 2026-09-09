import math
import random
print(abs(-1))
print(math.ceil(100.4))
print(math.floor(100.4))         
print(max(1,2,3))
print(min(1,2,3))
print(math.sqrt(32))
print(random.random())
print(random.randrange(1,10))
#exercises
def absdiff(x,y) :
    return abs(x - y)

result = absdiff(-999,33)
print(f"the absolute difference between -999 and 33 is: {result}")

def minmaxlist(numlist) :
    return max(numlist), min(numlist)
min,max = minmaxlist([1,2,3,4,5,25])
print(f"the minimum is {min}")
print(f"the maximum is {max}")

def squirt(num):
    if num < 0 :
        return "neg numbers aint supported"
    return math.sqrt(num)
result = squirt(256)
print(f"the square root is {result}")
