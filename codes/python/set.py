# create an empty set
s = set()

# add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

# output will be {1, 2, 3, 4}

# add duplicate elements to set
s.add(3)
# duplicate elements are ignored, that is, they are not added to the set

# output will still be {1, 2, 3, 4}

# remove elements from set
s.remove(2)
# output will be {1, 3, 4}

# print the set
print(s)

# print the length of the set
print(f"The set has {len(s)} elements.")