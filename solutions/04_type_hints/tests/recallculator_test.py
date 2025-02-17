import pytest
from recallculator import Recallculator


@pytest.fixture
def calculator():
    return Recallculator()


@pytest.fixture
def calculator_with_operations():
    calculator = Recallculator()
    for x in range(5):
        calculator.add(1, x)
    return calculator


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


def test_repr_for_a_used_instance(calculator_with_operations):
    assert repr(calculator_with_operations) == "<Recallculator, operations: 5>"


def test_inspect_prints_the_operations(calculator_with_operations, capsys):
    """
    To read more about capturing output from pytest, see
    https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html
    """
    calculator_with_operations.inspect()
    captured = capsys.readouterr()
    expected = "1 + 4\n1 + 3\n1 + 2\n1 + 1\n1 + 0\n"
    assert captured.out == expected


def test_inspect_returns_the_instance(calculator_with_operations):
    assert calculator_with_operations.inspect() == calculator_with_operations
