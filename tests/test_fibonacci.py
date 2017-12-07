import pytest
from my_app_tests.fibonacci import fib

def test_output_type():
    assert type(fib(7)) is list

def test_lengh():
    assert len(fib(7)) == 7

@pytest.mark.parametrize("test_input,expected", [
    (3.1, 0),
    ("string argument",0),
    (0,0)
])
def test_arguments(test_input, expected):
    assert len(fib(test_input)) == expected
