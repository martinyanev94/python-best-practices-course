def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You can't divide by zero!")
class NegativeValueError(Exception):
    pass

def calculate_square_root(value):
    if value < 0:
        raise NegativeValueError("Cannot calculate square root of a negative number!")
    return value ** 0.5
