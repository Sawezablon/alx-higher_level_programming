#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    len = len(sys.argv) - 1
    if len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        sum = add(a, b)
        print("{} + {} = {}".format(a, b, sum))
    if sys.argv[2] == "-":
        sum = sub(a, b)
        print("{} + {} = {}".format(a, b, sum))
    if sys.argv[2] == "*":
        sum = mul(a, b)
        print("{} + {} = {}".format(a, b, sum))
    if sys.argv[2] == "/":
        sum = div(a, b)
        print("{} + {} = {}".format(a, b, sum))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
