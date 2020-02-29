#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#
# https://leetcode.com/problems/coin-change-2/description/
#
# algorithms
# Medium (45.50%)
# Likes:    1139
# Dislikes: 46
# Total Accepted:    68.8K
# Total Submissions: 150.9K
# Testcase Example:  '5\n[1,2,5]'
#
# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that
# amount. You may assume that you have infinite number of each kind of
# coin.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# Example 2:
# 
# 
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# 
# 
# Example 3:
# 
# 
# Input: amount = 10, coins = [10] 
# Output: 1
# 
# 
# 
# 
# Note:
# 
# You can assume that
# 
# 
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
# 
# 
#
"""
与Combination Sum类似
"""
# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = []
        if amount == 0 and not coins:
            return 1
        if amount < 0:
            return len(res)
        if not coins:
            return len(res)
        
        self.dfs(amount, coins, 0, [], res)

        return len(res)

    def dfs(self, amount: int, 
            coins: List[int], 
            start: int, 
            curr: List[int], 
            res: List[List[int]]):
        if amount < 0:
            return 
        if amount == 0:
            res.append(curr.copy())
            return

        for i in range(start, len(coins)):
            curr.append(coins[i])
            self.dfs(amount - coins[i], coins, i, curr, res)    # 同一种硬币可以出现多次，所以从i开始，而不是i+1开始
            curr.pop()
        

"""another dfs version"""     
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.cnt = 0        # 为什么这里如果不定义全局变量就不行呢？
        self.dfs(coins, amount, 0, [])
        return self.cnt
    
    def dfs(self, coins, amount, startIndex, curr):
        if amount < 0:
            return
        
        if amount == 0:
            self.cnt += 1
            return
        
        for i in range(startIndex, len(coins)):
            curr.append(coins[i])
            self.dfs(coins, amount - coins[i], i, curr)
            curr.pop()

            
"""DP: not working, don't know why..."""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)         # dp[i] = how many ways get i
        dp[0] = 1
        
        for num in range(1, amount + 1):
            for coin in coins:
                if num - coin >= 0:
                    dp[num] += dp[num - coin]

        return dp[amount]   
    
"""DP: working, why...""" 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)         # dp[i] = how many ways get i
        dp[0] = 1
        
        for coin in coins:
            for num in range(1, amount + 1):
                if num - coin >= 0:
                    dp[num] += dp[num - coin]

        return dp[amount]    
