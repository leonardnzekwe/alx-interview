#!/usr/bin/python3
"""
island_perimeter(grid) Module:
that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    island_perimeter function:
    that returns the perimeter of the island described in grid

    Args:
        grid (list of list of integers): a list of list of integers

    Returns:
        int: perimeter of the island described in grid
    """
    row_len = len(grid)
    col_len = len(grid[0])
    perimeter = 0

    for row in range(row_len):
        for col in range(col_len):
            if grid[row][col] == 1:
                perimeter += 4

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
    return perimeter
