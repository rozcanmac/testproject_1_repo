# Calculator Program in Python

class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.calculate("add", 5, 3))
    print(calculator.calculate("subtract", 10, 4))
    print(calculator.calculate("multiply", 8, 2))
    print(calculator.calculate("divide", 16, 4))