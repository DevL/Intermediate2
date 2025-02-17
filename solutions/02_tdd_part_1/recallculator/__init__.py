class Recallculator:
    def __init__(self):
        self.operations = []

    def add(self, a, b):
        self.operations = [f"{a} + {b}"] + self.operations
        return a + b
