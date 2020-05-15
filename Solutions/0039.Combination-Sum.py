#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (52.26%)
# Likes:    2815
# Dislikes: 87
# Total Accepted:    441K
# Total Submissions: 840.9K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#


"""
Combination Sum 限制了组合中的数之和
Subsets 一个数只能选一次，Combination Sum 一个数可以选很多次
• 搜索时从 index 开始而不是从 index + 1
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        self.dfs(candidates, target, 0, [], res)

        return res

    # 1. 递归的定义：在candidates[start ... n-1] 中找到所有的组合，他们的和为 target
    # 和前半部分的 curr 拼起来放到 results 里
    # （找到所有以 curr 开头的满足条件的组合，放到 results
    def dfs(self, candidates, target, startIndex, curr, res):
        # 3. 递归的出口: target <= 0
        if target < 0:
            return

        if target == 0:
            res.append(curr.copy())     # deep copy
            return
        
        # 2. 递归的拆解：挑一个数放到curr里去，下面的for循环是必背的dfs + backtracking 模板
        for i in range(startIndex, len(candidates)):
            # 这条判断可有可无，加上的话程序会更快。如果当前这个元素大于target，那就不用再往后再加元素了。
            if candidates[i] > target:        
                continue
            curr.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, curr, res)      # 这里的start是从i开始的，而不是subsets里面的i+1, 这是因为Subsets 一个数只能选一次，Combination Sum 一个数可以选很多次
            curr.pop()


"""
不把res传入dfs参数中，这样可以简化dfs的传入参数
"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.dfs(nums, target, 0, [])
        return self.res
    
    def dfs(self, nums, target, startIdx, curr):
        if target < 0:
            return
        
        if target == 0:
            self.res.append(curr.copy())
            return
            
        for i in range(startIdx, len(nums)):
            if nums[i] > target:
                continue
                
            curr.append(nums[i])
            self.dfs(nums, target - nums[i], i, curr)
            curr.pop()
