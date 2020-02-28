#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (44.74%)
# Likes:    1256
# Dislikes: 52
# Total Accepted:    274.5K
# Total Submissions: 611.4K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        nums = sorted(candidates)

        self.dfs(nums, target, 0, [], res)

        return res

    def dfs(self, nums, target, startIndex, curr, res):
        if target < 0:
            return
        if target == 0:
            res.append(curr.copy())
            return
        
        for i in range(startIndex, len(nums)):
            # 去掉重复的输出,eg: [1,7,7], target=8, 保证只输出一个[1,7]，去重的方法与Subsets II中是一样的。 
            if i != 0 and nums[i] == nums[i-1] and i != startIndex:
                continue
                
            if nums[i] > target:
                continue
                
            curr.append(nums[i])
            self.dfs(nums, target - nums[i], i + 1, curr, res)
            curr.pop()
