#!/usr/bin/python3
""" Pascal's triangle """


def pascal_triangle(n):
    """
    Function that returns a list of integers
    representing the Pascal's triangle of n
        Parameters:
            n (int): Integer representing size
            Pascal's triangle

        Returns:
            triangle (list): List of integers
    """

    triangle = []
    if (n <= 0):
        return triangle
    triangle = [[1]]
    if (n == 1):
        return triangle
    for i in range(1, n):
        next = []
        pres = 0
        for x in triangle[-1]:
            next.append(pres + x)
            pres = x
        next.append(pres)
        triangle.append(next)
    return triangle
