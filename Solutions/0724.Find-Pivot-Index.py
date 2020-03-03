#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
# https://leetcode.com/problems/find-pivot-index/description/
#
# algorithms
# Easy (42.40%)
# Likes:    825
# Dislikes: 187
# Total Accepted:    101.3K
# Total Submissions: 238.1K
# Testcase Example:  '[1,7,3,6,5,6]'
#
# Given an array of integers nums, write a method that returns the "pivot"
# index of this array.
# 
# We define the pivot index as the index where the sum of the numbers to the
# left of the index is equal to the sum of the numbers to the right of the
# index.
# 
# If no such index exists, we should return -1. If there are multiple pivot
# indexes, you should return the left-most pivot index.
# 
# Example 1:
# 
# 
# Input: 
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation: 
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the
# sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# nums = [1, 2, 3]
# Output: -1
# Explanation: 
# There is no index that satisfies the conditions in the problem
# statement.
# 
# 
# 
# 
# Note:
# 
# 
# The length of nums will be in the range [0, 10000].
# Each element nums[i] will be an integer in the range [-1000, 1000].
# 
# 
# 
# 
#

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lens = len(nums)
        prefixSum = [0] * (lens + 1)
        for i in range(lens):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
            
        for i in range(lens):
            leftSum = prefixSum[i]      # prefixSum[i]是不包括nums[i]的
            rightSum = prefixSum[-1] - prefixSum[i] - nums[i]      
            if leftSum == rightSum:
                return i
            
        return -1
