#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (56.83%)
# Likes:    2719
# Dislikes: 64
# Total Accepted:    462.1K
# Total Submissions: 810.5K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
"""模板的DFS + back tracking求combination问题"""
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for length in range(n + 1):
            self.dfs(nums, length, 0, [], res)
        
        return res

    def dfs(self, nums, length, index, curr, res):
        if len(curr) == length:
            res.append(curr.copy())
            return
        
        for i in range(index, len(nums)):
            curr.append(nums[i])
            self.dfs(nums, length, i + 1, curr, res)
            curr.pop()


# @lc code=end

