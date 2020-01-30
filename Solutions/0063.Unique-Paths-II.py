63. Unique Paths II

题目是62 加上一个obstacle，有的地方是过不去的。

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

解法：过不去的地方设为dp[i][j] = 0 就可以了
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]        # 确定状态：f[i][j]表示达到(i, j)位置的方法数
        
        dp[0][0] = 1                            # 初始化
        for i in range(1, m):                   # 初始化：on the first col，分两种情况讨论
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][0] = 0
                
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]
            else:
                dp[0][j] = 0
                
        for row in range(1, m):                 
            for col in range(1, n):
                if obstacleGrid[row][col] == 1:     # 转移方程：也要分两种情况讨论
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]      
                    
        return dp[-1][-1]
