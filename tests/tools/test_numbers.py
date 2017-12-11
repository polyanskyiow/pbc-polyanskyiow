import pytest
from pbc.tools.numbers import print_pairs

@pytest.mark.print_pairs
def test_output_type():
    assert type(print_pairs(2,7,5,3,1,5,9,8,1)) is set

@pytest.mark.print_pairs
@pytest.mark.parametrize("test_input,expected", [
    ( (2,7,5,3,1,5,9,8,1) , 4),
    ( (1,2,3,4,5) , 0),
    ( (5,5,5,5,5) , 1)
])

@pytest.mark.print_pairs
def test_lengh_with_pairs(test_input, expected):
    assert len(print_pairs(*test_input)) == expected
