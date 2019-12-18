Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


"""grandyang DP: dp[i]表示组成i的完全平方数的最小个数
递推公式：dp[i+j**2] = dp[i]+1
初始值：dp[1] = 1;  返回值：dp[n+1]"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [5] * (n+1)   # 四平方和定理：任意一个正整数均可表示为4个整数的平方和，其实是可以表示为4个以内的平方数之和，那么就是说返回结果只有 1,2,3 或4其中的一个
        dp[0], dp[1] = 0, 1   # 这里必须从dp[0]=0开始算，不然dp[4]就无法等于1了！
        for i in range(0, n+1):
            j = 1
            while i+j**2 <= n:
                dp[i+j**2] = min(dp[i+j**2], dp[i] + 1)
                j += 1
        return dp[-1]
