import argparse
from my_app_tests.fibonacci import fib
from my_app_tests.numbers_pairs import print_pairs


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This app prints a number to the output")
    group = parser.add_argument_group("Parameters")
    group.add_argument("--fib",  action='store_true',  help="Print predetermined count of fibonacci numbers")
    group.add_argument("--number", "-n", action='store', help="A number to print", type=int)
    group.add_argument("--pairs", action='store_true', help="Print filtered (without duplicates) pairs with sum=10")
    group.add_argument("--arguments", "-arg", action='store', nargs='+', help="Sequence of numbers, should be like: 1 2 3 7 8 9", type=int)
    args = parser.parse_args()
    args.fib
    if(args.fib):
        print( fib(args.number) )
    if (args.pairs):
        print( print_pairs(*args.arguments))
