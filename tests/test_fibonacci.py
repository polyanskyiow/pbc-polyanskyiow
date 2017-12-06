from my_app_tests.fibonacci import fib

def test_output_type():
    assert type(fib(7)) is list

def test_lengh():
    assert len(fib(7)) == 7

def test_float_as_argument():
    assert len(fib(3.1)) == 0

def test_sting_as_argument():
    assert len(fib('string argument')) == 0

def test_zero_as_argument():
    assert len(fib(0)) == 0