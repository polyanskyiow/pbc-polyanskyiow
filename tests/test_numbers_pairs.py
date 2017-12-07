import pytest
from my_app_tests.numbers_pairs import print_pairs

def test_output_type():
    assert type(print_pairs(2,7,5,3,1,5,9,8,1)) is set

@pytest.mark.parametrize("test_input,expected", [
    ( (2,7,5,3,1,5,9,8,1) , 4),
    ( (1,2,3,4,5) , 0),
    ( (5,5,5,5,5) , 1)
])
def test_lengh_with_pairs(test_input, expected):
    assert len(print_pairs(*test_input)) == expected
