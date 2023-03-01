#!/usr/bin/python3

"""Calculates the perimeter of an island"""


def island_perimeter(grid):
    """Island perimeter"""

    perimeter = 0

    if grid is None:
        return 0
    if len(grid) == 0:
        return 0
    for i in range(len(grid)):
        if grid[i] is None:
            continue
        if grid[i][0] == 1:
            perimeter += 1

        if grid[i][-1] == 1:
            perimeter += 1

        for j in range(len(grid[i])):
            if (i == 0):
                if grid[i][j] == 1:
                    perimeter += 1

            if i == (len(grid) - 1):
                if grid[i][j] == 1:
                    perimeter += 1

            if i != (len(grid) - 1):
                if grid[i][j] != grid[i+1][j]:
                    perimeter += 1

            if j != (len(grid[i]) - 1):
                if grid[i][j] != grid[i][j+1]:
                    perimeter += 1

    return perimeter
