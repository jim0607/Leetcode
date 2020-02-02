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


"""brutal force: O(M*N*(M+N))"""
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        res, tempCnt = 0, 0
        for i in range(m):
            for j in range(n):                
                if grid[i][j] == "0":
                    tempCnt = 0
                    
                    # look up
                    row, col = i, j
                    while row >= 0:
                        if grid[row][col] == "W":
                            break
                        elif grid[row][col] == "E":
                            tempCnt += 1
                        row -= 1
                    
                    # look down
                    row, col = i, j
                    while row < m:
                        if grid[row][col] == "W":
                            break
                        elif grid[row][col] == "E":
                            tempCnt += 1
                        row += 1
                    
                    # look left:
                    row, col = i, j
                    while col >= 0:
                        if grid[row][col] == "W":
                            break
                        elif grid[row][col] == "E":
                            tempCnt += 1
                        col -= 1
                        
                    # look right:
                    row, col = i, j
                    while col < n:
                        if grid[row][col] == "W":
                            break
                        elif grid[row][col] == "E":
                            tempCnt += 1
                        col += 1
                            
                res = max(res, tempCnt)
                    
        return res
                        
                        
                        
"""DP解法
up[i][j]=在(i,j)位置能向上炸的敌人数目
if (i,j) 是墙：up[i][j] = 0
if (i,j) 是空地：up[i][j] = 0; up[i][j] += up[i-1][j]
if (i,j) 是敌人：up[i][j] = 1; up[i][j] += up[i-1][j] 
同理算出down[i][j], left[i][j], right[i][j]
然后能炸的敌人数目为up+down+left+right
O(M*N)"""
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        res = [[0] * n for _ in range(m)]
        
        # up
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "W":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 0
                    if grid[i][j] == "E":
                        dp[i][j] = 1
                    
                    if i - 1 >= 0:
                        dp[i][j] += dp[i - 1][j]
                        
                res[i][j] += dp[i][j]        
        
        # down
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if grid[i][j] == "W":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 0
                    if grid[i][j] == "E":
                        dp[i][j] = 1
                    
                    if i + 1 < m:
                        dp[i][j] += dp[i + 1][j]
                        
                res[i][j] += dp[i][j]
                        
        # left
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "W":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 0
                    if grid[i][j] == "E":
                        dp[i][j] = 1
                        
                    if j - 1 >= 0:
                        dp[i][j] += dp[i][j - 1]
                        
                res[i][j] += dp[i][j]
                
        # right
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == "W":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 0
                    if grid[i][j] == "E":
                        dp[i][j] = 1
                        
                    if j + 1 < n:
                        dp[i][j] += dp[i][j + 1]
                        
                res[i][j] += dp[i][j]
                
        maxRes = 0        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    maxRes = max(maxRes, res[i][j])
                    
        return maxRes  
