# How to use lambda functions in Python to represent functions efficiently
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# function to sort the people by name
def f(person):
    return person["name"]

# function to sort the people by house
def f(person):
    return person["house"]

# sort the people by name
people.sort(key=f)

print(people)


# output will be for sort by name:
# [{'name': 'Cho', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'}, {'name': 'Harry', 'house': 'Gryffindor'}]

# output will be for sort by house:
# [{'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Cho', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'}]



# lamda expressions
# lambda functions are functions that are defined in one line
# they are useful when you want to pass a function as an argument to another function
# for example, if you want to sort a list of people by name, you can use a lambda function
# lambda functions are defined using the keyword lambda

# sort the people by name
people.sort(key=lambda person: person["name"])