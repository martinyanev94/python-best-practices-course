expression = Subtraction(
    Multiplication(
        Addition(Number(5), Number(3)),
        Division(Number(10), Number(2))
    ),
    Subtraction(Number(2), Number(1))
)

result = expression.interpret()
print(f"The result of the expression is: {result}")
