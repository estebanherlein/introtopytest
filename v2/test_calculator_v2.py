import calculator


def test_add():
    result = calculator.add(8, 2)
    expected = 10
    assert result == expected

def test_substract():
    result = calculator.subtract(8, 2)
    expected = 6
    assert result == expected

def test_multiply():
    result = calculator.multiply(8, 2)
    expected = 16
    assert result == expected

def test_divide():
    result = calculator.divide(8, 2)
    expected = 4
    assert result == expected