import pytest


def my_sum(a, b):
    return a + b


def my_mul(a, b):
    return a * b


def my_expo(a, b):
    return a ** b


@pytest.mark.parametrize('function, params, result',
                         [
                             (my_sum, (2, 4), 6),
                             (my_mul, (2, 4), 8),
                             (my_expo, (2, 4), 16),
                         ])
def test_functions(function, params, result):
    assert function(*params) == result
