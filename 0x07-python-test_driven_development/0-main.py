#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(7, 20))
print(add_integer(1.5,2.8))
print(add_integer(6.3, 8.5))
print(add_integer(3.2, 2))
print(add_integer(4, 1.7))
try:
    print(add_integer("Hello", 2))
except Exception as e:
    print(e)
try:
    print(add_integer(1, "Holbies"))
except Exception as e:
    print(e)