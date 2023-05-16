#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(triangle):
    """
    Print the triangle
    """
    dp = []
    if triangle <= 0:
        return dp
    
    dp = [[1]]
    for i in range(1, triangle):
        new_row = [1]
        for j in range(1, i):
            new_row.append(dp[i-1][j]+dp[i-1][j-1])
            
        new_row.append(1)
        dp.append(new_row)
        
    return dp
