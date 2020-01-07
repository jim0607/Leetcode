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
• 加入一个新的参数来限制
Subsets 无重复元素，Combination Sum 有重复元素
• 需要先去重
Subsets 一个数只能选一次，Combination Sum 一个数可以选很多次
• 搜索时从 index 开始而不是从 index + 1
"""
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if not candidates or target <= 0:
            return []

        # 去重
        # python可以用一句话实现: nums = sorted(set(candidates))
        # 自己实现的话采用快慢双指针法
        nums = self.removeDuplicates(candidates)

        self.dfs(nums, target, 0, [], res)

        return res

    # 1. 递归的定义：在candidates[start ... n-1] 中找到所有的组合，他们的和为 target
    # 和前半部分的 curr 拼起来放到 results 里
    # （找到所有以 curr 开头的满足条件的组合，放到 results
    def dfs(self, nums, target, start, curr, res):
        # 3. 递归的出口: target <= 0
        if target < 0:
            return

        if target == 0:
            res.append(curr.copy())     # deep copy
            return
        
        # 2. 递归的拆解：挑一个数放到curr里去，下面的for循环是必背的dfs + backtracking 模板
        for i in range(start, len(nums)):
            # 这条判断可有可无，加上的话程序会更快。如果当前这个元素大于target，那就不用再往后再加元素了。
            if nums[i] > target:        
                break
            curr.append(nums[i])
            self.dfs(nums, target - nums[i], i, curr, res)      # 这里的start是从i开始的，而不是subsets里面的i+1, 这是因为Subsets 一个数只能选一次，Combination Sum 一个数可以选很多次
            curr.pop()

    # 快慢双指针法：leetcode 26
    def removeDuplicates(self, candidates):
        candidates = sorted(candidates)
        slow = 0
        for fast in range(1, len(candidates)):
            if candidates[slow] != candidates[fast]:
                slow += 1
                candidates[slow] = candidates[fast]

        return candidates[:slow+1]

        
# @lc code=end

