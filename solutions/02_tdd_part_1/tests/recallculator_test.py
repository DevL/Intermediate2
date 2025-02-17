from recallculator import Recallculator


def test_a_new_instance_has_not_performed_any_operations():
    calculator = Recallculator()
    assert calculator.operations == []


def test_addition():
    calculator = Recallculator()
    assert calculator.add(1, 2) == 3


def test_registering_addition():
    calculator = Recallculator()
    calculator.add(1, 2)
    assert "1 + 2" in calculator.operations


def test_registering_multiple_operations():
    calculator = Recallculator()
    calculator.add(3, 4)
    calculator.add(5, 6)

    expected = ["5 + 6", "3 + 4"]
    assert calculator.operations == expected
