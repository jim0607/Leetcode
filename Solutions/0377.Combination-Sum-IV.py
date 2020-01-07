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

# @lc code=start
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
        
# @lc code=end

