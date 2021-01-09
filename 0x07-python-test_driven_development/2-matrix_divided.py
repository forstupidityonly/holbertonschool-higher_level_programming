#!/usr/bin/python3
"""matrix divide module"""


def matrix_divided(matrix, div):
    """
        return new matrix made from old matrix divided by 'div'
        raises
            must be a list of lists of integers or floats, otherwise raise a
        TypeError--
            Each row of the matrix must be of the same size, otherwise raise a TypeError
        div must be a number (integer or float), otherwise raise a TypeError
        div can’t be equal to 0, otherwise raise a ZeroDivisionError
    """
    error_message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise TypeError(error_message)
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(error_message)
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(error_message)

    row_len = len(matrix[0])
    for i in matrix:
        if len(i) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return[[round(item / div, 2) for item in list] for list in matrix]
