"""
174. Dungeon Game

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
"""

"""
find the max of mininum_sum in all the paths.
这题不能像1102.Path-With-Maximum-Minimum-Value那样用Dijkstra's (mnlogn)因为这题不是四个方向都能走的，
也就是说选择了一个方向就不能回到原来的位置了，所以只能dp -O(mn).
https://www.youtube.com/watch?v=qx8VCY-zScA
假设我们能到达(m, n)房间，我们需要的最小血量是dp[m][n] = 1 if A[m][n] >= 0 else 1- A[m][n], 这是我们的base case.
那我们就知道了我们到达(m-1, n)房间所需的最小血量是dp[m-1][n] = 到达(m, n)房间所需要的血量减去在(m-1, n)房间的损耗，
即dp[m-1][n] =max(dp[m][n] - A[m-1][n], 1); 到达(m, n-1)房间所需的最小血量是dp[m][n-1] = max(dp[m][n] - A[m][n-1], 1).
所以我们是从终点倒着往起点推。
"""
class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[m-1][n-1] = max(1, 1 - grid[m-1][n-1])
        for i in range(m - 2, -1, -1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - grid[i][n-1])
        for j in range(n - 2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - grid[m-1][j])        
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = min(max(1, dp[i+1][j] - grid[i][j]), max(1, dp[i][j+1] - grid[i][j]))
        return dp[0][0]
