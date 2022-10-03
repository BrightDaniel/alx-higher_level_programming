#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print(" ".join("{:d}".format(j) for j in i))
