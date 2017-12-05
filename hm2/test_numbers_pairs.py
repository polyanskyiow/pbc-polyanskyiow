from hm1.numbers_pairs import print_pairs

def test_output_type():
    assert type(print_pairs(10, 2,7,5,3,1,5,9,8,1)) is set

def test_lengh_with_pairs():
    assert len(print_pairs(10, 2,7,5,3,1,5,9,8,1)) == 4

def test_lengh_with_no_pairs():
    assert len(print_pairs(10, 1,2,3,4,5)) == 0

def test_no_duplicates():
    assert len(print_pairs(10, 5,5,5,5,5)) == 1