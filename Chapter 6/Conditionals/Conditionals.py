# aka shorthand if statements
# use of logical opperators in if statements
# also nested if statements
# where are the case and switch? ={
# we are just gonna go straight to the exercizes

# exercise 1 execpt its an allegory to the new verification process most apps now require
age = int(input("This is a hold up (you live in the EU/UK)! Age NOW: "))

if age < 18:
    print("Child!")
elif age >= 18 and age < 65:
    print("Child! ([Click Here] to appeal via Personal Data\nThis will be deleted and not sold trust me bro)")
else:
    print("Senior! (We really don't care about you anyways)")

     # exercise 2
num1 = float(input("enter number:"))
num2 = float(input("enter another number:"))
op = input("what operation (+ - * /):")

if op == "+":
 print(f"the sum is {num1 + num2}")
elif op == "-":
 print(f"the difference is {num1 - num2}")
elif op == "*":
 print(f"the product is {num1 * num2}")
elif op == "/":
    if num2 != 0:
        print(f"the quotient is {num1 / num2}")
    else:
        print("oi no dividing by zero!")
else:
    print("Thats not a valid operator my guy")

    # exercise 3
veg = input("are you a vegetarian? ").lower()

if veg == 'yes':
    eggs = input("ok now do you eat eggs? ").lower()
    if eggs == 'yes':
        print("veggie omelette")
    else:
        print("have a veggie stir-fry and these vitamin pills cause you are getting ZERO amino acids")
else:
    print("steak")