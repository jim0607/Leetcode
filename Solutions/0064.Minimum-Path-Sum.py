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


"""
dp[i][j] means the minimum path sum to (i, j)
dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
O(N^2), O(N^2)
"""
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        dp[0][0] = grid[0][0]
            
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                    
                # 前面都是初始化，初始化的是左边和上边，要学会在主for循环里面初始化
                
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                
        return dp[-1][-1]
"""


"""空间优化：由于dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
也就是说dp[i][j]只与他的前一行有关，所以计算得到了了dp[7]之后，就可以吧dp[6]之前都删掉了，因为再需要计算dp[8]的时候用不到，所以dp每次只需要保存一行数组用于后面的计算就可以了。如何实现呢？我们是用滚动数组：一开始不要开m行，之开两行dp[0][]和dp[1][]两行，初始化dp[0][]，计算dp[1][]，然后计算dp[2][]的时候就不需要dp[0][]了，把dp[2][]存到dp[0][]里面就可以了
空间就优化为O(N)了"""
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(2)]        # 只开两行
                  
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                    
                elif j == 0:
                    if i % 2 == 1:
                        dp[1][j] = dp[0][j] + grid[i][j]
                    else:
                        dp[0][j] = dp[1][j] + grid[i][j]
                    
                # 以上是初始化左边和上边
                
                else:
                    if i % 2 == 1:
                        dp[1][j] = min(dp[0][j], dp[1][j - 1]) + grid[i][j]
                    else:
                        dp[0][j] = min(dp[1][j], dp[0][j - 1]) + grid[i][j]
                
        return dp[1][-1] if m % 2 == 0 else dp[0][-1]      
"""


"""继续做空间优化：由于dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
也就是说dp[i][j]只与他的前一列有关，也可以用滚动数组的方法优化列
空间就优化为O(1)了，后面和以思考"""
