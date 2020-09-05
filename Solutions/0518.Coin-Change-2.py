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
solution 1: just print all combinations - O(N*2^N)
"""
class Solution:
    def change(self, target: int, nums: List[int]) -> int:
        def backtrack(curr_idx, curr_comb, curr_sum):
            if curr_sum == target:
                res.append(curr_comb.copy())
                return
            
            if curr_sum > target:
                return
            
            for next_idx in range(curr_idx, len(nums)):     # 同一个数可以重复出现，所以可以从curr_idx开始
                if nums[next_idx] > target:
                    continue
                curr_comb.append(nums[next_idx])
                backtrack(next_idx, curr_comb, curr_sum + nums[next_idx])
                curr_comb.pop()
                
                
        res = []
        backtrack(0, [], 0)
        return len(res)




"""DP: not working, don't know why..."""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)         # dp[i] = how many ways get i
        dp[0] = 1
        
        # 这样会有一个问题，那就是(1,3)可以进solution, (3,1)也可以进solution
        # 想想num=4的时候, 当coin遍历到coin=1时dp[4]+=dp[1]
        # coin遍历到coin=3时dp[4]+=dp[3]，此时dp[3]已经被更新过一次了，里面就带有dp[1]的信息了
        for num in range(1, amount + 1):
            for coin in coins:      
                if num - coin >= 0:   # 这里会导致(1,3)可以进solution, (3,1)也可以进solution
                    dp[num] += dp[num - coin]

        return dp[amount]   
    
"""DP: working, why...""" 
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)         # dp[i] = how many ways get i
        dp[0] = 1
        
        # 这样写可以保证避开(1,3)和(3,1)的问题，因为当coin遍历到coin=1的时候，dp[4]+=d[3]此时的dp[3]=0所以dp[4]实际上加的是0
        # 而当coin遍历到coin=3的时候，dp[4]+=d[1]，此时d[1]被更新过一次。所以真个过程dp[4]只被更新一次，不会重复更新。
        for coin in coins:      
            for num in range(1, amount + 1):
                if num - coin >= 0:
                    dp[num] += dp[num - coin]

        return dp[amount]    


        

"""another dfs version"""     
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.cnt = 0        # 为什么这里如果不定义全局变量就不行呢？因为int is immutable
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

            

