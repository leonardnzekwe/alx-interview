#!/usr/bin/python3
"""Paschal Triangle Module"""


def pascal_triangle(n):
    """paschal_triangle function"""
    triangle_list = []
    if n > 0:
        for i in range(n):
            row = [1] * (i + 1)
            if i >= 2:
                for j in range(1, i):
                    row[j] = (
                        triangle_list[i - 1][j - 1] + triangle_list[i - 1][j]
                    )
            triangle_list.append(row)
    return triangle_list
