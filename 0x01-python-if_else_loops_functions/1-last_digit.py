#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
last = number % 10 if number > 0 else int(repr(number)[-1]) * -1
if (last > 5):
    print("{} {:d} is {:d} and is greater than 5"
        .format(str, number, last))
elif (last == 0):
    print("{} {:d} is {:d} and is 0"
        .format(str, number, last))
else:
    print("{} {:d} is {:d} and is less than 6 and not 0"
        .format(str, number, last))