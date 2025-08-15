class Shape:
    def area(self, shape):
        if isinstance(shape, Square):
            return shape.side * shape.side
        elif isinstance(shape, Circle):
            return 3.14 * shape.radius * shape.radius
        raise ValueError("Unknown shape")

class Square:
    def __init__(self, side):
        self.side = side

class Circle:
    def __init__(self, radius):
        self.radius = radius

calculator = Shape()
print(calculator.area(Square(5)))  # Output: 25
print(calculator.area(Circle(3)))   # Output: 28.26
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def calculate_area(shapes):
    for shape in shapes:
        print(f"Area: {shape.area()}")

shapes = [Square(5), Circle(3), Rectangle(4, 6)]
calculate_area(shapes)
