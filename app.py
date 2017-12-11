import argparse
from pbc.tools.fibonacci import fib
from pbc.tools.numbers import print_pairs

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="App can return a Fibonacci sequence with given length "
                                                 "or find numbers pair with  specified sum")

    subparsers = parser.add_subparsers(help='sub-command help')

    parser_fib = subparsers.add_parser("fib", help="Print predetermined count of fibonacci numbers")
    parser_fib.add_argument("--number", "-n", action="store", help="A number for print", type=int)
    parser_fib.set_defaults(which='fib')

    parser_pairs = subparsers.add_parser("print_pairs", help="Return pairs with specified sum.")
    parser_pairs.add_argument("--arguments", "-arg", action='store', nargs='+', help="Sequence of numbers, should be like: 1 2 3 7 8 9", type=int)
    parser_pairs.set_defaults(which="print_pairs")

    args = parser.parse_args()

    if args.which == "fib":
        print(fib(args.number))
    elif args.which == "print_pairs":
        print(print_pairs(*args.arguments))

