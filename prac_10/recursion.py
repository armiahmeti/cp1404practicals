
"""
CP1404/CP5632 Practical - Enhanced Solution
Recursion tasks.
"""

def do_it(n):
    """Calculate sum of n % 2 recursively."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

def calculate_blocks(rows):
    """Calculate blocks for a pyramid recursively."""
    if rows <= 0:
        return 0
    return rows + calculate_blocks(rows - 1)
