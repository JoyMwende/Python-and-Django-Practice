# How to handle exceptions in Python
import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    # exit the program
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # exit the program
    sys.exit(1)

print(f"{x} / {y} = {result}")

# example of exception is when you divide by zero and you get a ZeroDivisionError e.g 10/0
# another example is when you try to convert a string to an integer e.g int("foo") and you get a ValueError
# to handle these exceptions, you can use a try and except block