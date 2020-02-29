#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (43.44%)
# Likes:    1476
# Dislikes: 51
# Total Accepted:    299.4K
# Total Submissions: 686.9K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
"""
输入数组中带重复元素的permutation
"""
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()     # !!!!!输入里面有重复，都需要先把数组排序一下

        visited = {i: False for i in range(len(nums))}
        self.dfs(nums, [], res, visited)

        return res

    def dfs(self, nums, curr, res, visited):
        if len(curr) == len(nums):
            res.append(curr.copy())
            return

        for i in range(len(nums)):
            # 首先这个数visited过了自然要continue
            # 然后如果这个数与它前一个数是一样的但是前一个数并没有放进去，那就不要把这个数放进去了，因为我们是优先放前面的那个数。
            if visited[i] or (i != 0 and nums[i] == nums[i-1] and not visited[i-1]):
                continue

            curr.append(nums[i])
            visited[i] = True
            self.dfs(nums, curr, res, visited)
            curr.pop()
            visited[i] = False
        
# @lc code=end

