"""•要求从一些正整数中选出一些，使得和是Target
• 背包问题
• 数组A：各个物品的重量
• Target：背包最大称重
Given n distinct positive integers, integer k (k <= n) and a number target.

Find k numbers where sum is target. Calculate how many solutions there are?

Have you met this question in a real interview?  
Example
Example 1

Input:
List = [1,2,3,4]
k = 2
target = 5
Output: 2
Explanation: 1 + 4 = 2 + 3 = 5


"""•要求从一些正整数中选出一些，使得和是Target
• 背包问题
• 数组A：各个物品的重量
• Target：背包最大称重
• 使得和是Target：背包正好装满
• 最后一步：最后一个数An-1是否选入这K个数
• 情况一（An-1不选入）：需要在前n-1个数中选K个数，使得它们的和
是Target
• 情况二（An-1选入）：需要在前n-1个数中选K-1个数，使得它们的和是
Target - An-1
• 要知道还有几个数可选，以及它们的和需要是多少：序列加状态
• 状态：f[i][j][s]表示有多少种方法可以在前i个数中选出j个，使得它们
的和是s
f[i][j][s] = f[i-1][j][s]; if s>=A[i-1]: f[i][j][s] += f[i-1][k-1][s-A[i-1]] """
class Solution:
    def kSum(self, A, k, target):
        lens = len(A)
        dp = [[[0] * (target + 1) for _ in range(k + 1)] for _ in range(lens + 1)]

        for i in range(lens + 1):
            for j in range(k + 1):
                for s in range(target + 1):
                    if j == 0 and s == 0:
                        dp[i][j][s] = 1
                        continue
                    
                    if i >= 1:
                        dp[i][j][s] += dp[i - 1][j][s]
                        
                        if s >= A[i - 1] and j >= 1:
                            dp[i][j][s] += dp[i - 1][j - 1][s - A[i - 1]]

        return dp[lens][k][target]
