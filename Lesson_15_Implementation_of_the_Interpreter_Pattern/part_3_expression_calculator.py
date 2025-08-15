expression = Subtraction(
    Addition(Number(5), Number(3)),
    Subtraction(Number(2), Number(1))
)

result = expression.interpret()
print(f"The result of the expression is: {result}")
