#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (44.15%)
# Likes:    1056
# Dislikes: 126
# Total Accepted:    103K
# Total Submissions: 233.1K
# Testcase Example:  '[1,2,3]\n4'
#
# Given an integer array with all positive numbers and no duplicates, find the
# number of possible combinations that add up to a positive integer target.
# 
# Example:
# 
# 
# nums = [1, 2, 3]
# target = 4
# 
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 
# Note that different sequences are counted as different combinations.
# 
# Therefore the output is 7.
# 
# 
# 
# 
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?
# 
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test
# cases.
# 
#


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = []
        if not nums or target <= 0:
            return len(res)
        
        self.dfs(nums, target, 0, [], res)

        return len(res)

    def dfs(self, nums: List[int], target: int, start: int, curr: List[int], res: List[List[int]]):
        if target < 0:
            return

        if target == 0:
            res.append(curr.copy())
        
        # 遍历所有已i开头的可能的curr
        for i in range(start, len(nums)):
            curr.append(nums[i])
            self.dfs(nums, target - nums[i], 0, curr, res)      # 顺序不重要（(1, 3)和(3, 1)都可以），所以让i从0开始
            curr.pop()       
        

"""
不要求输出所有的combination，所以除了dfs，还有更快的方法：背包问题。
如果问题要求用i个数加在一起拼出target，那么多半是背包问题。
f[i]=how many ways to combine to number i  背包问题一定要把总承重放到状态里！！
f[i]=f[i-A1]+f[i-A2]+f[i-A3]....
f[0] = 1
return f[target]
这个题其实和coin change那题是一样的。
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        dp = [0] * (target + 1)
        
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
                    
        return dp[target]
