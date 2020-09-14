120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.



class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[float("inf")] * (i+1) for i in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            for j in range(len(triangle[i])):
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + triangle[i][j])
                if j < len(triangle[i]) - 1:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + triangle[i][j])
        return min(dp[-1])











class Solution:
    def minimumTotal(self, A: List[List[int]]) -> int:
        dp = []
        for row in A:
            dp.append(row)
            
        for i in range(1, len(A)):
            for j in range(len(A[i])):
                if j == 0:
                    dp[i][j] += dp[i - 1][j]
                elif j == len(A[i]) - 1:
                    dp[i][j] += dp[i - 1][j - 1]
                else:
                    dp[i][j] += min(dp[i - 1][j], dp[i - 1][j - 1])
                    
        return min(dp[len(A) - 1])



另一种写法：
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * len(triangle[i]) for i in range(len(triangle))]
                
        dp[0][0] = triangle[0][0]
        
        for i in range(1, len(triangle)):
            dp[i][0] = triangle[i][0] + dp[i - 1][0]
            dp[i][-1] = triangle[i][-1] + dp[i - 1][-1]
            for j in range(1, len(triangle[i]) - 1):
                dp[i][j] = min(triangle[i][j] + dp[i - 1][j], triangle[i][j] + dp[i - 1][j - 1])
                
        return min(dp[-1])



Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
Rolling array to reduce the space to O(N)
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0] * m for _ in range(2)]
        dp[0][m - 1] = triangle[0][0]
        
        for i in range(1, m):
            dp[i % 2][m - len(triangle[i])] = dp[(i - 1) % 2][m - len(triangle[i]) + 1] + triangle[i][0]
            dp[i % 2][-1] = dp[(i - 1) % 2][-1] + triangle[i][-1]
            
            for j in range(1, len(triangle[i]) - 1):
                dp[i % 2][m - j - 1] = min(dp[(i - 1) % 2][m - j - 1], dp[(i - 1) % 2][m - j]) + triangle[i][j]
                
        return min(dp[(m - 1) % 2])
