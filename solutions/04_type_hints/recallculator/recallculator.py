from typing import Union

Number = Union[int, float]


class Recallculator:
    """
    A class for performing and keeping track of simple arithmetic calculations.

    Arithmetic operations performed by the methods add, subtract, multiply,
    and divide are available via the operations property.
    """

    def __init__(self):
        self._operations = []

    @property
    def operations(self) -> list[str]:
        """
        The performed operations in reverse order as strings.

        >>> callculator = Recallculator()
        >>> _ = callculator.add(1, 2)
        >>> _ = callculator.subtract(3, 4)
        >>> callculator.operations
        ['3 - 4', '1 + 2']
        """
        return self._operations

    def add(self, a: Number, b: Number) -> Number:
        """
        Registers an addition operation and returns the sum of two numbers.

        >>> Recallculator().add(1, 2)
        3
        """
        self._register_operation("+", a, b)
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        """
        Registers a subtraction operation and returns the difference of two numbers.

        >>> Recallculator().subtract(1, 2)
        -1
        """
        self._register_operation("-", a, b)
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        """
        Registers a multiplication operation and returns the product of two numbers.

        >>> Recallculator().multiply(1, 2)
        2
        """
        self._register_operation("*", a, b)
        return a * b

    def divide(self, a: Number, b: Number) -> float:
        """
        Registers a division operation and returns the quotient of two numbers.

        >>> Recallculator().divide(1, 2)
        0.5
        """
        self._register_operation("/", a, b)
        return a / b

    def inspect(self):
        for operation in self.operations:
            print(operation)
        return self

    def _register_operation(self, operand, a, b):
        self._operations = [f"{a} {operand} {b}"] + self._operations

    def __repr__(self):
        return f"<{self.__class__.__name__}, operations: {len(self._operations)}>"
