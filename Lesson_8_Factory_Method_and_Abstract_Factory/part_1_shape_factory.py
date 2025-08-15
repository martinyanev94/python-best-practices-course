class Shape:
    def draw(self):
        raise NotImplementedError("This method should be overridden.")

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class ShapeFactory:
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Square":
            return Square()
        return None

# Client code
shape = ShapeFactory.get_shape("Circle")
print(shape.draw())
