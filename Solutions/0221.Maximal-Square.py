Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4


"""dp[i][j] 表示到在 (i, j) 位置所能组成的最大正方形的边长。返回max(dp)
初始条件是边角上的dp[i][j] = int(matrix[i][j])
只有当前 (i, j) 位置为1，dp[i][j] 才有可能大于0，否则 dp[i][j] 一定为0。当 (i, j) 位置为1，此时要看 dp[i-1][j-1], dp[i][j-1]，和 dp[i-1][j] 这三个位置，我们找其中最小的值，并加上1，就是 dp[i][j] 的当前值了，这个并不难想，毕竟不能有0存在，所以只能取交集，最后再用 dp[i][j] 的值来更新结果 res 的值即可。"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1 if matrix[i][j] == "1" else 0
                    continue
                    
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                 
        maxArea = 0
        for i in range(m):
            for j in range(n):
                maxArea = max(maxArea, dp[i][j]**2)
                    
        return maxArea
