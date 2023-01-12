#!/usr/bin/python3
""" Minimum operations """


def minOperations(n: int) -> int:
    """
    A method that calculates the fewest
    number of operations needed to result
    in exactly n H characters in the file.

    Parameters:
    n (int): Number of H required in file

    Returns:
        Minimum number of steps
    """
    if n % 1 > 0:
        return 0
    return int(findMin(n)[0])


def findMin(n):
    """
    Find minimum operations
    """

    i: int = 2
    while (n % i > 0):
        i += 1
    if i < n:
        ret = findMin(n/i)
        if ret[1] * i == n:
            ret = ret[0] + i, ret[1] * i, ret[1]
    else:
        ret = n, n, 1
    return ret
