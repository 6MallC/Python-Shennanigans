# choice, cycle, Control
# python has a dedicatied 
import random

x = 10
for i in range(x):
 if i<5:
     print('x is less than 5')
 elif i == 5 :
     print('x is equal to 5')
 else:
     print('x is greater than 5')
     break
     
while x >= 1:
    print(x)
    x -= 1

#exercises
grade = int(input("Grade Time: "))  
if grade >= 90:
    print("damned good job")
elif grade >= 70:
    print("I mean its alright")
else:
    print("regret")

#  exercise 2 
y = 0
for i in range(1,101):
    y += i
print("sum= ", y)

# exercise 3 
target = random.randrange(1,20)
guess = None

while guess != target:
    guess = int(input("Im thinking of a number between 1 and 20. What is it? "))

    if guess < target:
        print("Too low!")
    elif guess > target:
        print("Too high")
    else:
        print("Noice")