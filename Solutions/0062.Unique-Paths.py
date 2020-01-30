62. Unique Paths

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right



"""
• 最后一步：无论机器人用何种方式到达右下角，总有最后挪动的一步：
– 向右 或者 向下
• 右下角坐标设为(m-1, n-1)
• 那么前一步机器人一定是在(m-2, n-1)或者(m-1, n-2)
• 那么，如果机器人有 X 种方式从左上角走到(m-2,n-1)，有 Y 种方式从左上角走到(m-1,n-2)，则机器人有 X+Y 种方式走到(m-1, n-1)
• 问题转化为子问题，机器人有多少种方式从左上角走到(m-2, n-1)和(m-1, n-2)
• 原题要求有多少种方式从左上角走到(m-1, n-1)

• 状态：设f[i][j]为机器人有多少种方式从左上角走到(i, j)"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]      # 确定状态：f[i][j]为机器人有多少种方式从左上角走到(i, j)
        for i in range(m):                  # 初始条件：只有一种方法走到行为0或者列为0的地方，因为不能往左走也不能往上走
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
            
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
                
        return dp[-1][-1]
