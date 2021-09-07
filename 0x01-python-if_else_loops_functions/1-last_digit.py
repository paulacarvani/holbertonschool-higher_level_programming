#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sent = "Last digit of"
if number >= 0:
    last = number % 10
else:
    last = number % -10
if last == 0:
    print("{} {:d} is {:d} and is 0".format(sent, number, last))
elif last > 5:
    print("{} {:d} is {:d} and is greater than 5".format(sent, number, last))
elif last < 6 and last != 0:
    print("{} {:d} is {:d} and is less than 6 and not 0"
    .format(sent, number, last))
