#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    if not matrix:
        return None
    return list(list(map(lambda x: x*x, new_mat)) for new_mat in matrix)
