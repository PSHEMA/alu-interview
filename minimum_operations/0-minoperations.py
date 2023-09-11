#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    i = 2

    while i <= n:
        if n % i == 0:
            n //= i
            operations += i
        else:
            i += 1

    return operations
