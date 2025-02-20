class Recallculator:
    def __init__(self):
        self.operations = []

    def add(self, a, b):
        self.operations = [f"{a} + {b}"] + self.operations
        # OR: self.operations.insert(0, f"{a} + {b}")
        return a + b
