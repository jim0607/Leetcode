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
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(curr_idx, curr_comb, curr_sum):
            if curr_sum == target:
                res.append(curr_comb.copy())
                return
            
            if curr_sum > target:
                return
            
            for next_idx in range(curr_idx + 1, len(nums)):     # 一个数只能用一次所以从curr_idx + 1开始
                if next_idx > 0 and nums[next_idx] == nums[next_idx-1] and next_idx - 1 != curr_idx:
                    continue                        # 去重第二步
                    
                if nums[next_idx] > target:     # strong prune
                    continue
                curr_comb.append(nums[next_idx])
                backtrack(next_idx, curr_comb, curr_sum + nums[next_idx])
                curr_comb.pop()
                
        
        nums.sort()     # 去重第一步是sort        
        res = []
        backtrack(-1, [], 0)
        return res




class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.backtrack(nums, target, 0, [])
        return self.res
    
    def backtrack(self, nums, target, startIdx, curr):
        if target < 0:
            return
        
        if target == 0:
            self.res.append(curr.copy())
            return
        
        for i in range(startIdx, len(nums)):
            if nums[i] > target or (i >= 1 and nums[i] == nums[i-1]) and i != startIdx:
                continue
                
            curr.append(nums[i])
            self.backtrack(nums, target - nums[i], i + 1, curr)
            curr.pop()
