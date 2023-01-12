#!/usr/bin/python3
""" Minimum operations """


def open_boxes(n: int) -> int:
    """
    A method that calculates the fewest
    number of operations needed to result
    in exactly n H characters in the file.

    Parameters:
    n (int): Number of H required in file

    Returns:
        Minimum number of steps
    """
    H_n: int = 1

    while (H_n < n):
        H_n *= 2
        if (H_n == n):
            return 
    return 0
