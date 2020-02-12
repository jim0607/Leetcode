213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
             
             
            
"""与House robber I 相比，这个题目的房子形成了一个环，所以第一个房子和第N个房子不能同时偷，我们可以把问题分成两个问题来解决：
1. 房子1没偷：问题变成了对房子2~N做House robber I的问题
2. 房子N没偷：问题变成了对房子1~N-1做House robber I的问题"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        lens = len(nums)
        if lens == 1:
            return nums[0]
        if lens == 2:
            return max(nums[0], nums[1])
        
        res = 0
        # sub-problem 1: didn't rob house 1: find the max for house 2~N
        prevMax, currMax = 0, 0
        for num in nums[1:]:
            temp = currMax
            currMax = max(prevMax + num, currMax)       # dp[i] = max(dp[i-2]+num, dp[i-1])
            prevMax = temp
        
        res = currMax
        
        # sub-problem 2:didn't rob house N: find hte max for house 1~N-1
        prevMax, currMax = 0, 0
        for num in nums[:lens - 1]:
            temp = currMax
            currMax = max(prevMax + num, currMax)
            prevMax = temp
            
        res = max(res, currMax)
        
        return res
