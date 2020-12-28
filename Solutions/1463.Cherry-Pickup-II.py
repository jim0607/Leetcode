"""
1463. Cherry Pickup II

Given a rows x cols matrix grid representing a field of cherries. 
Each cell in grid represents the number of cherries that you can collect.

You have two robots that can collect cherries for you, Robot #1 is located at the top-left corner (0,0) , 
and Robot #2 is located at the top-right corner (0, cols-1) of the grid.

Return the maximum number of cherries collection using both robots  by following the rules below:

From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an empty cell (0).
When both robots stay on the same cell, only one of them takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in the grid.

Example 1:

Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.
Example 2:

Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.
Example 3:

Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
Output: 22
Example 4:

Input: grid = [[1,1],[1,1]]
Output: 4
 
Constraints:

rows == grid.length
cols == grid[i].length
2 <= rows, cols <= 70
0 <= grid[i][j] <= 100 
"""



"""
dp[i][j1][j2] = the max cherry when robot reached (i, j1) and (i, j2)
"""
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * n for _ in range(n)] for _ in range(m)]
        dp[0][0][n-1] = grid[0][0] + grid[0][n-1]
        
        for i in range(1, m):
            for j1 in range(n):
                for j2 in range(n):
                    curr_cherry = grid[i][j1] + grid[i][j2] if j1 != j2 else grid[i][j1]    # A, B在同一点只能pick up 一次
                    for prev_j1 in [j1 - 1, j1, j1 + 1]:
                        for prev_j2 in [j2 - 1, j2, j2 + 1]:
                            if 0 <= prev_j1 < n and 0 <= prev_j2 < n:
                                if dp[i-1][prev_j1][prev_j2] >= 0:  # 这里debug了1 hour, >= 0 表示(prev_j1, prev_j2)可以到达, 也就代表可以作为prev位置走到curr位置
                                    dp[i][j1][j2] = max(dp[i][j1][j2], dp[i-1][prev_j1][prev_j2] + curr_cherry)
                    
        max_cherry = 0
        for j1 in range(n):
            for j2 in range(j1 + 1, n):
                max_cherry = max(max_cherry, dp[-1][j1][j2])
        return max_cherry
       
       
       
"""
dp[i][j1][j2] = the max cherry we can pick up for robots ended at (i, j1), (i, j2)
"""
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1] * n for _ in range(n)] for _ in range(m)]
        dp[0][0][-1] = grid[0][0] + grid[0][-1]
        for i in range(0, m - 1):
            for j1 in range(n):
                for j2 in range(n):
                    if dp[i][j1][j2] != -1:     # j1, j2 could be reached
                        for next_j1 in [j1 - 1, j1, j1 + 1]:
                            for next_j2 in [j2 - 1, j2, j2 + 1]:
                                if 0 <= next_j1 < n and 0 <= next_j2 < n:
                                    next_cherry = grid[i+1][next_j1] + grid[i+1][next_j2] if next_j1 != next_j2 else grid[i+1][next_j1]   # A, B在同一点只能pick up 一次
                                    dp[i+1][next_j1][next_j2] = max(dp[i+1][next_j1][next_j2], dp[i][j1][j2] + next_cherry)
        
        max_cherry = 0
        for j1 in range(n):
            for j2 in range(n):
                max_cherry = max(max_cherry, dp[-1][j1][j2])
        return max_cherry
