import pytest
from recallculator import Recallculator


@pytest.fixture
def calculator():
    return Recallculator()


def test_a_new_instance_has_not_performed_any_operations(calculator):
    assert calculator.operations == []


def test_add_is_documented():
    assert Recallculator.add.__doc__


def test_subtract_is_documented():
    assert Recallculator.add.__doc__


def test_multiply_is_documented():
    assert Recallculator.add.__doc__


def test_divide_is_documented():
    assert Recallculator.add.__doc__


def test_operations_is_documented():
    assert Recallculator.operations.__doc__


def test_the_class_is_documented():
    assert Recallculator.__doc__


def test_the_package_is_documented():
    import recallculator

    assert recallculator.__doc__


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
