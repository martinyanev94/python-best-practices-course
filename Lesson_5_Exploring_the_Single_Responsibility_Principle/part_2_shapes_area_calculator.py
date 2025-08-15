class Shape:
    def __init__(self, shape_type, dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def area(self):
        if self.shape_type == 'rectangle':
            width, height = self.dimensions
            return width * height
        elif self.shape_type == 'circle':
            radius, = self.dimensions
            return 3.14 * (radius ** 2)

    def display_area(self):
        print(f"The area of the {self.shape_type} is: {self.area()}")
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class AreaCalculator:
    @staticmethod
    def calculate_area(shape):
        return shape.area()

class AreaDisplay:
    @staticmethod
    def display_area(shape):
        print(f"The area of the shape is: {shape.area()}")
