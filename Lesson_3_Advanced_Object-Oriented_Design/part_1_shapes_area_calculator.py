class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# This should work
def print_area(rectangle):
    print(f"The area is: {rectangle.area()}")

rect = Rectangle(4, 5)
print_area(rect)

square = Square(5)
print_area(square)
