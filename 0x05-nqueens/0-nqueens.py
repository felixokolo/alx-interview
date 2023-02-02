#!/usr/bin/python3
""" Code to solve the nqueens challenge"""

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)
N = sys.argv[1]
if not N.isnumeric():
    print('N must be a number')
    exit(1)
N = int(N)
if N < 4:
    print('N must be at least 4')
    exit(1)


def get_enemies(pos):
    enemies = []
    for i in range(N):
        enemies.append([i, pos[1]])
        enemies.append([pos[0], i])
    if pos[0] > pos[1]:
        start = [max(pos)-min(pos), 0]
    else:
        start = [0, max(pos)-min(pos)]
    while min(start) >= 0 and max(start) < N+1:
        enemies.append(start.copy())
        start[0] += 1
        start[1] += 1
    start = pos.copy()
    while min(start) >= 0 and max(start) < N+1:
        start[0] -= 1
        start[1] += 1
    start[0] += 1
    start[1] -= 1
    while min(start) >= 0 and max(start) < N+1:
        enemies.append(start.copy())
        start[0] += 1
        start[1] -= 1
    return enemies


def accept(Parent, child):
    enemies = get_enemies(child)
    for i in Parent:
        if i in enemies:
            return False
    else:
        return True


def find_solution(Parent, pos):
    """ find solution of challenge"""
    if len(Parent) == N:
        return Parent
    for i in range(N):
        if accept(Parent, [pos+1, i]):
            Parent.append([pos+1, i])
            ret = find_solution(Parent, pos+1)
            if ret is None:
                del Parent[-1]
                continue
            else:
                return ret
    else:
        return None
    return ret


for i in range(N):
    print(find_solution([[0, i]], 0))
