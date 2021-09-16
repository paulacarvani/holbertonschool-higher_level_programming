#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    num_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum, item = 0, 0
    for i in roman_string:
        if num_r[i] > item:
            sum += num_r[i] - item * 2
        else:
            sum += num_r[i]
        item = num_r[i]
    return sum
