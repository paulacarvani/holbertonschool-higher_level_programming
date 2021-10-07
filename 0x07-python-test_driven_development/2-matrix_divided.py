#!/usr/bin/python3
"""Module that creates a function
to divides all elements of a matrix
Matrix must be a list of int or floats
Each row of the matrix has to be the same len
Return mus be a int and not 0"""


def matrix_divided(matrix, div):
    """Return a new matrix with all values divided by `div`.
    Matrix must be a list of lists.
    Each sub-list must contain only integers or floats.
    Empty sub-lists are not allowed.
    Divisor must be greater than 0 and must be an int or float.
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
