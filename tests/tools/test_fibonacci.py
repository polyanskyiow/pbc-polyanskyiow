import pytest
from pbc.tools.fibonacci import fib

@pytest.mark.fibonacci
def test_output_type():
    assert type(fib(7)) is list

@pytest.mark.fibonacci
def test_lengh():
    assert len(fib(7)) == 7

@pytest.mark.fibonacci
@pytest.mark.parametrize("test_input,expected", [
    (3.1, 0),
    ("string argument",0),
    (0,0)
])

@pytest.mark.fibonacci
def test_arguments(test_input, expected):
    assert len(fib(test_input)) == expected
