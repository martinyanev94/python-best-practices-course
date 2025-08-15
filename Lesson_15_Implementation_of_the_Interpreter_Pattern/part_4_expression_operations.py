class Multiplication(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() * self.right.interpret()

class Division(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self):
        right_value = self.right.interpret()
        if right_value == 0:
            raise ValueError("Cannot divide by zero.")
        return self.left.interpret() / right_value
