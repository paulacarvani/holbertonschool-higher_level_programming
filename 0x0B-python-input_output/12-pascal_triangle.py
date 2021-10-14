#!/usr/bin/python3
"""
Contains the pascal_triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle"""
    if n <= 0:
        return []

    limit = n - 1
    triangle = [
        [1]
        ]

    for i in range(limit):
        row = [1]

        if len(triangle[i]) > 1:
            len_row = len(triangle[i]) - 1

            for j in range(len_row):
                row.append(triangle[i][j] + triangle[i][j + 1])

        row.append(1)
        triangle.append(row)
    return triangle
