#!/usr/bin/python3
import random
number = -98#random.randint(-10000, 10000)
n = number
if number < 0:
    num = number * -1
    num = num % 10
    last = num * -1
    if num == 0:
        print(f"Last digit of {number} is {last} and is 0")
    else:
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
else:
    if number % 10 > 5:
        print(f"Last digit of {number} is {number % 10} and is greater than 5")
    elif number % 10 == 0:
        print(f"Last digit of {number} is {number % 10} and is 0")
    else:
        print(f"Last digit of {n} is {n % 10} and is less than 6 and not 0")
