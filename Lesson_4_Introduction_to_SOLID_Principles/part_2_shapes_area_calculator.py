class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

def calculate_area(shape: Rectangle) -> float:
    return shape.width * shape.height
from math import pi
from typing import Protocol

class Shape(Protocol):
    def area(self) -> float:
        ...

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height

    def area(self) -> float:
        return self.width * self.height

class Circle:
    def __init__(self, radius: float):
        self.radius: float = radius

    def area(self) -> float:
        return pi * (self.radius**2)

def calculate_area(shape: Shape) -> float:
    return shape.area()

if __name__ == "__main__":
    rect = Rectangle(12, 8)
    print(f"Rectangle area: {calculate_area(rect)}")

    circ = Circle(6.5)
    print(f"Circle area: {calculate_area(circ):.2f}")
