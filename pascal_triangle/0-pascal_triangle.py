#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ Pascal's Triangle """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(n):
        new_row = [1]
        for j in range(len(triangle[i]) - 1):
            new_row.append(triangle[i][j] + triangle[i][j + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
