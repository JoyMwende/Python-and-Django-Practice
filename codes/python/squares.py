# importing functions from another file
# import a specific function from a file called functions
from functions import square

for i in range(10):
    print(f"The sqaure of {i} is {square(i)}")

# the function is going to loop 10 times


# alternatively:
# import the whole file/module
import functions

for i in range(10):
    print(f"The square of {i} is {functions.square(i)}") # indicate the function you are using from the imported file


# you can also import modules from csv files and other files we have not written