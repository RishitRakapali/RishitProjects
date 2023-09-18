import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return ('<' + self.__class__.__name__ + ' x=' + str(self.x) + ' y=' + str(self.y) + '>')
    def area(self):
        pass
    def circumference(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    def __repr__(self):
        return ('<' + self.__class__.__name__ +
                ' x=' + str(self.x) + ' y=' + str(self.y) + ' radius=' + str(self.radius) + '>')
    def area(self):
        return math.pi * (self.radius ** 2)
    def circumference(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width
    def __repr__(self):
        return ('<' + self.__class__.__name__ + ' x=' + str(self.x) + ' y=' + str(self.y) +
                ' height=' + str(self.height) + ' width=' + str(self.width) + '>')
    def area(self):
        return self.height * self. width
    def circumference(self):
        return 2 * (self.height + self.width)

class Triangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width
    def __repr__(self):
        return ('<' + self.__class__.__name__ + ' x=' + str(self.x) + ' y=' + str(self.y) +
                ' height=' + str(self.height) + ' width=' + str(self.width) + '>')
    def area(self):
        return (self.height * self.width) / 2
    def circumference(self):
        return math.sqrt((self.height ** 2) + (self.width ** 2)) + self.height + self. width

class Square(Rectangle):
    def __init__(self, x, y, height, width):
        super().__init__(x, y, height, width)
    def __repr__(self):
        return ('<' + self.__class__.__name__ + ' x=' + str(self.x) + ' y=' + str(self.y) +
                ' height=' + str(self.height) + ' width=' + str(self.width) + '>')

TestShape = Shape(5, 10)
print(TestShape)
print(TestShape.area())
print(TestShape.circumference())
print()
TestCircle = Circle(5, 10, 70)
print(TestCircle)
print(TestCircle.area())
print(TestCircle.circumference())
print()
TestTriangle = Triangle(5, 10, 50, 20)
print(TestTriangle)
print(TestTriangle.area())
print(TestTriangle.circumference())
print()
TestRectangle = Rectangle(5, 10, 50, 20)
print(TestRectangle)
print(TestRectangle.area())
print(TestRectangle.circumference())
print()
TestSquare = Square(5, 10, 50, 20)
print(TestSquare)
print(TestSquare.area())
print(TestSquare.circumference())
print()

# Polymorphism
print(TestShape.area())
print(TestCircle.area())
print(TestTriangle.area())
print(TestRectangle.area())
print(TestSquare.area())
print()
print(TestShape.circumference())
print(TestCircle.circumference())
print(TestTriangle.circumference())
print(TestRectangle.circumference())
print(TestSquare.circumference())


