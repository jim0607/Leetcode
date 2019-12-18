Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        len_row = len(grid)
        len_col = len(grid[0])
        res = 0
        for i in range(len_row):
            for j in range(len_col):
                cnt = 0
                if grid[i][j] == "0":
                    m = i-1
                    while m >= 0:
                        if grid[m][j] == "E":
                            cnt += 1
                            m -= 1
                        elif grid[m][j] == "0":
                            m -= 1
                        else:
                            break
                    m = i+1
                    while m < len_row:
                        if grid[m][j] == "E":
                            cnt += 1
                            m += 1
                        elif grid[m][j] == "0":
                            m += 1
                        else:
                            break
                    n = j-1
                    while n >= 0:
                        if grid[i][n] == "E":
                            cnt += 1
                            n -= 1
                        elif grid[i][n] == "0":
                            n -= 1
                        else:
                            break
                    n = j+1
                    while n < len_col:
                        if grid[i][n] == "E":
                            cnt += 1
                            n += 1
                        elif grid[i][n] == "0":
                            n += 1
                        else:
                            break
                res = max(res, cnt)
        return res
