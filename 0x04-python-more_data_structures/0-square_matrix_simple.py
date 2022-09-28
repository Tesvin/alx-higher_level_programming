#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    i = 0
    for i in matrix:
        newmatrix.append([])
        for x in matrix[i]:
            newmatrix[i].append(y**2)
        i += 1
    return (newmatrix)
