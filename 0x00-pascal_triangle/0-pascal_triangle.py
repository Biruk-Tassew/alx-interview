#!/usr/bin/python3

"""
0-pascal_triangle
"""

def print_triangle(triangle):
    """
    Print the triangle
    """
    
    dp = [[1]]
        
    for i in range(1, numRows):
        new_row = [1]
        for j in range(1, i):
            new_row.append(dp[i-1][j]+dp[i-1][j-1])
            
        new_row.append(1)
        dp.append(new_row)
        
    return dp
