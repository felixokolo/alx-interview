#!/usr/bin/python3
"""Prime number game"""


def isWinner(x, nums):
    """Gets the widder of the game"""

    players = {'Maria': 0, 'Ben': 0}
    if ((x is None or x == 0 or
         nums is None or len(nums) == 0)):
        return None
    for i in range(x):
        arr = list(range(1, nums[i]+1))
        primes = [j for j in arr if isPrime(j)]
        if len(primes) % 2 == 1:
            winner = 'Maria'
        else:
            winner = 'Ben'
        players[winner] = players[winner] + 1
    if players['Maria'] > players['Ben']:
        return 'Maria'
    else:
        return 'Ben'


def isPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(3, x):
        if x % i == 0:
            return False
    else:
        return True


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
