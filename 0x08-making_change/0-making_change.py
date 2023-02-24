#!/usr/bin/python3

"""Gets the minimum coins to make change"""


def makeChange(coins, total):
    """Function to get minimum change"""
    if total is None or total == 0:
        return 0
    if total < 0:
        return 0
    if len(coins) == 0:
        return -1
    sorted_coins = coins.copy()
    sorted_coins.sort(reverse=True)
    pres = 0
    num = 0
    for i in sorted_coins:
        if (pres + i) > total:
            continue
        rem = total - pres
        mul = rem // i
        if mul == 0:
            return -1
        num += mul
        pres += mul * i
        if pres == total:
            return num
    return -1
