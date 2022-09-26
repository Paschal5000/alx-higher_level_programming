#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in numpy.matrix(matrix):
            print("{:d}".format(i))
