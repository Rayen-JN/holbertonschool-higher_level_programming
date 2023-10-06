#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    NEW = matrix.copy()

    for i in range(len(matrix)):
        NEW[i] = list(map(lambda x: x**2, matrix[i]))

    return (NEW)

