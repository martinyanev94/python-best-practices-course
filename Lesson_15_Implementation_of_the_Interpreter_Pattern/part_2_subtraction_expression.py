class Subtraction(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()
class Number(Expression):
    def __init__(self, value: int):
        self.value = value

    def interpret(self):
        return self.value
