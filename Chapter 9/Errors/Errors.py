# try block executes code to check for errors if returns true exepts below code and finnally is code that will always run
#straight to exercises


def read(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("no file lmao")
read("a_real_file_trust.txt")

def divi():
    try:
        x = float(input("first number: "))
        y = float(input("second number: "))
        z = x/y
        print(f"result is {z}")
    except ZeroDivisionError:
        print("the answer is 0 according to that one math teacher trust me")
    except ValueError:
        print("no")
divi()

#these next ones are dupes

list = [2,"20",0,"apple", 3]

try:
    for item in list:
        try:
            print(int(item))
        except ValueError:
            print(f"cant convert {item} to int")
#execpt Execption as e:
#   print(f"you messed up i think {e}")

finally:
    print("all done")

    



