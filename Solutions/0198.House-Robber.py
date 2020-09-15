"""
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
             
             
             

"""f[i]=the max profit when reaching ith house
f[i] = max(rob ith, not rob ith)
f[i] = max(f[i-2]+nums[i], f[i-1])"""
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) == 1:
            return dp[0]
        
        dp[1] = max(nums[1], nums[0])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            
        return dp[-1]
        
"""
"""空间优化：dp[i] 之和 dp[i-2]与dp[i-1]有关，所以可以用prevMax和currMax来代表dp[i-2]与dp[i-1]"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        prevMax, currMax = 0, 0 # prevMax is dp[i-2], currMax is dp[i-1]
        for i in range(len(nums)):
            temp = currMax
            currMax = max(prevMax + nums[i], currMax)
            prevMax = temp
            
        return currMax
