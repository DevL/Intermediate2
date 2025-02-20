class Recallculator:
    def __init__(self):
        self._operations = []

    @property
    def operations(self):
        return list(reversed(self._operations))

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
        self._operations.append(f"{a} {operand} {b}")

    def __repr__(self):
        return f"<{self.__class__.__name__}, operations: {len(self._operations)}>"
