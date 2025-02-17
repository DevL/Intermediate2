class Recallculator:
    def __init__(self):
        self.operations = []

    def add(self, a, b):
        self._register_operation("+", a, b)
        return a + b

    def subtract(self, a, b):
        self._register_operation("-", a, b)
        return a - b

    def multiply(self, a, b):
        self._register_operation("*", a, b)
        return a * b

    def divide(self, a, b):
        self._register_operation("/", a, b)
        return a / b

    def _register_operation(self, operand, a, b):
        self.operations = [f"{a} {operand} {b}"] + self.operations
