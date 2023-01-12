#!/usr/bin/python3
""" Minimum operations """


def minOperations(n):
    """
    A method that calculates the fewest
    number of operations needed to result
    in exactly n H characters in the file.

    Parameters:
    n (int): Number of H required in file

    Returns:
        Minimum number of steps
    """
    i: int = 2
    while (n % i > 0):
        i += 1
    if i < n:
        ret = minOperations(n/i) + i
    else:
        ret = n
    return int(ret)


    
