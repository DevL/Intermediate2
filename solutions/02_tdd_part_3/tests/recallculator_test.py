import pytest
from recallculator import Recallculator


@pytest.fixture
def calculator():
    return Recallculator()


def test_a_new_instance_has_not_performed_any_operations(calculator):
    assert calculator.operations == []


def test_addition(calculator):
    assert calculator.add(1, 2) == 3


def test_registering_addition(calculator):
    calculator.add(1, 2)
    assert "1 + 2" in calculator.operations


def test_subtraction(calculator):
    assert calculator.subtract(3, 4) == -1


def test_registering_subtraction(calculator):
    calculator.subtract(3, 4)
    assert "3 - 4" in calculator.operations


def test_multiplication(calculator):
    assert calculator.multiply(2, 5) == 10


def test_registering_multiplication(calculator):
    calculator.multiply(2, 5)
    assert "2 * 5" in calculator.operations


def test_division(calculator):
    assert calculator.divide(5, 4) == 1.25


def test_registering_division(calculator):
    calculator.divide(5, 4)
    assert "5 / 4" in calculator.operations


def test_registering_multiple_operations(calculator):
    calculator.add(3, 4)
    calculator.subtract(5, 6)
    calculator.multiply(7, 8)
    calculator.divide(9, 10)

    expected = [
        "9 / 10",
        "7 * 8",
        "5 - 6",
        "3 + 4",
    ]
    assert calculator.operations == expected


def test_repr_for_an_unused_instance(calculator):
    assert repr(calculator) == "<Recallculator, operations: 0>"


def test_repr_for_a_used_instance(calculator):
    for x in range(5):
        calculator.add(1, x)
    assert repr(calculator) == "<Recallculator, operations: 5>"
