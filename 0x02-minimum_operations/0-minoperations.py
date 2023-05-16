#!/usr/bin/python3

"""
Minimum Operations
Given num n, write a method that calculates the fewest number of operations
needed to result in exactly n H characters in a file
Prototype: def min_operations(n)
Returns an integer
if n is impossible to achieve, return 0
"""


def minOperations(n):
    """
    Function min_operations
    Returns an integer
    """
    result = 0
    x = 2
    while n > 1:
        while not n % x:
            result += x
            n /= x
        x += 1
    return result
