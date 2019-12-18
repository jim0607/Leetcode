You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1


"""方法一：自下而上，时间复杂度：O(S*n)。空间复杂度：O(S)，dp 使用的空间。"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]表示amount = i时最少的组合方法数
        # 递推关系是dp[i] = dp[i-coin]+1
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount]==float("inf") else dp[amount]
"""还有BFS,DFS的算法，后面可以多思考一下"""
