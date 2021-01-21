import calculator
import pytest


@pytest.mark.parametrize("first_input,second_input,expected",
                         [(0, 1, 1), (1, 1, 2), (11, 3, 14), (998, 3, 1001),  (999, 0, 999), pytest.param(-7, 2, 42, marks=pytest.mark.xfail)])
def test_add(first_input, second_input, expected):
    result = calculator.add(first_input, second_input)
    assert result == expected


@pytest.mark.parametrize("first_input,second_input,expected",
                         [(1, 0, 1), (1, 1, 0), (11, 3, 8), (998, 9, 989), (999, 999, 0), pytest.param(4, 1000, 42, marks=pytest.mark.xfail)])
def test_substract(first_input, second_input, expected):
    result = calculator.subtract(first_input, second_input)
    assert result == expected


@pytest.mark.parametrize("first_input,second_input,expected",
                         [(1, 0, 0), (1, 1, 1), (11, 3, 33), (998, 2, 1996), (999, 999, 998001), pytest.param(5, -999, 42, marks=pytest.mark.xfail)])
def test_multiply(first_input, second_input, expected):
    result = calculator.multiply(first_input, second_input)
    assert result == expected


@pytest.mark.parametrize("first_input,second_input,expected",
                         [(0, 1, 0), (1, 1, 1), (12, 3, 4), (998, 2, 499), (999, 333, 3), pytest.param(1002, -101, 42, marks=pytest.mark.xfail)])
def test_divide(first_input, second_input, expected):
    result = calculator.divide(first_input, second_input)
    assert result == expected



