class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


# alternatively:
class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

# creatting a new point
p = Point(2, 8) # this is the same as Point.__init__(p, 2, 8) where you give the values of x and y
print(p.x)
print(p.y)