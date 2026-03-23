# calculator_program.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

class Calculator:
    def __init__(self):
        pass

    def calculate(self, operation, num1, num2):
        if operation == "add":
            return add(num1, num2)
        elif operation == "subtract":
            return subtract(num1, num2)
        elif operation == "multiply":
            return multiply(num1, num2)
        elif operation == "divide":
            return divide(num1, num2)

if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.calculate("add", 5, 3))
    print(calculator.calculate("subtract", 10, 4))
    print(calculator.calculate("multiply", 8, 2))
    print(calculator.calculate("divide", 16, 4))