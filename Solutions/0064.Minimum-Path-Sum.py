Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        len_row, len_col = len(grid), len(grid[0])

        if len_row == 1:
            return sum(grid[0][i] for i in range(len_col))
        if len_col == 1:
            return sum(grid[0][i] for i in range(len_row))
        
        dp = [[0]*len_col for _ in range(len_row)]
        dp[0][0] = grid[0][0]
        # 注意要先更新两个边的部分，因为每次只能向下或者向右移动一步， 所以可以更新
        for i in range(1, len_row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, len_col):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, len_row):
            for j in range(1, len_col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                
        return dp[len_row-1][len_col-1]
"""进阶：可否更新为一维甚至零维dp算法"""
