#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    arg = len(sys.argv) - 1
    if arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == "+":
        sum = add(a, b)
        print("{} + {} = {}".format(a, b, sum))
    elif sys.argv[2] == "-":
        sum = sub(a, b)
        print("{} + {} = {}".format(a, b, sum))
    elif sys.argv[2] == "*":
        sum = mul(a, b)
        print("{} + {} = {}".format(a, b, sum))
    else:
        sum = div(a, b)
        print("{} + {} = {}".format(a, b, sum))
