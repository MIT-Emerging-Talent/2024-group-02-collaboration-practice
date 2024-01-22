"""
grid_traveler.py
Usage:
from src.grid_traveler import grid_traveller_basic, grid_traveller_memo, grid_traveller_table
"""
def grid_traveller_basic(m: (int, float), n: int) -> int:
    """
    Basic recursive approach to calculate the number of ways to travel in a grid.

    Arguments:
        m (int ): Number of rows.
        n (int ): Number of columns.

    Returns:
        int: Number of ways to travel from the top-left to the bottom-right corner.
        >>>grid_traveller_basic(18, 18)
           2333606220
    """
    # Assertions 
    assert isinstance(m, int) and m > 0, "Number of rows (m) must be a positive integer."
    assert isinstance(n, int) and n > 0, "Number of columns (n) must be a positive integer."
    # if the grid is a single cell, there is only one way to travel
    if m == 1 and n == 1:
        return 1
    # then if any dimension is zero, there are zero ways to travel
    if m == 0 or n == 0:
        return 0
    # we sumup all the ways from the cell above and the cell to the left
    return grid_traveller_basic(m-1, n) + grid_traveller_basic(m, n-1)


def grid_traveller_memo(m: int, n: int, memo: dict = None) -> int:
    """
    Memoized recursive approach to calculate the number of ways to travel in a grid.

    Arguments:
        m (int): Number of rows.
        n (int): Number of columns.
        memo (dict): Memoization dictionary to store computed results.

    Returns:
        int: Number of ways to travel from the top-left to the bottom-right corner.
        >>>grid_traveller_memo(3, 3)
          6
    """
    #Assertions
    assert isinstance(m, int) and m > 0, "Number of rows (m) must be a positive integer."
    assert isinstance(n, int) and n > 0, "Number of columns (n) must be a positive integer."
    # initialize the memoization dictionary if it's not provided
    if memo is None:
        memo = {}
    # we check if the result for the current cell is already memoized in the dictionary
    if (m, n) in memo:
        return memo[(m, n)]
    #  if the grid is a single cell, there is only one way to travel
    if m == 1 and n == 1:
        return 1
    # if any dimension is zero, there are zero ways to travel
    if m == 0 or n == 0:
        return 0
    # sumup all ways from the cell above and the cell to the left
    result = grid_traveller_memo(m-1, n, memo) + grid_traveller_memo(m, n-1, memo)
    # save the result
    memo[(m, n)] = result
    return result

def grid_traveller_table(m: int, n: int) -> int:
    """
    Dynamic programming approach using a table to calculate the number of ways to travel in a grid.

    Arguments:
        m (int): Number of rows.
        n (int): Number of columns.

    Returns:
        int: Number of ways to travel from the top-left to the bottom-right corner.
        >>>grid_traveller_table(3,2)
        3
    """
    #Assertions
    assert isinstance(m, int) and m > 0, "Number of rows (m) must be a positive integer."
    assert isinstance(n, int) and n > 0, "Number of columns (n) must be a positive integer."
    # we create a table to store intermediate results
    table = [[0] * (n+1) for _ in range(m+1)]

    table[1][1] = 1

    # we fill the table 
    for i in range(1, m+1):
        for j in range(1, n+1):
            # we sumup ways from the cell above and the cell to the left
            table[i][j] += table[i-1][j] + table[i][j-1]

    # we get the result for the bottom-right corner
    return table[m][n]
