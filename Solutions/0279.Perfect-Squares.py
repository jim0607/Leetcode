279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.




"""f[i]=the least number os perfect square numbers which sum to i
f[j] = min(f[j-i^2]+1) for i^2<=j
Time complexity: j is from 0 to n, i is from 0 to j^0.5, so O(N^1.5)"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for j in range(2, n + 1):
            i = 1
            while i**2 <= j:
                dp[j] = min(dp[j], dp[j - i**2] + 1)
                i += 1
                
        return dp[n]
