import argparse
from my_app_tests.fibonacci import fib
from my_app_tests.numbers_pairs import print_pairs


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This app prints a number to the output")
    group = parser.add_argument_group("Parameters")
    group.add_argument("--fib",  action='store_true')
    group.add_argument("--number", "-n", action='store', help="A number to print", type=int)
    group.add_argument("--pairs", action='store', help="A number to print", type=int)
    args = parser.parse_args()
    args.fib
