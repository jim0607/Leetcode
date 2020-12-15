#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (55.84%)
# Likes:    2801
# Dislikes: 98
# Total Accepted:    595.6K
# Total Submissions: 1.1M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#


"""
下面这个解法是move non-zeros whenever we find one. 
这个解法可以maintain non-zero的relative order, 但是不能maintain zero的relative order
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[anchor] = nums[anchor], nums[i]
                anchor += 1
        return nums   


"""
下面这个解法是move zeros whenever we find one.
这个解法可以maintain zero的relative order, 但是不能maintain non-zero的relative order
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums[i], nums[anchor] = nums[anchor], nums[i]
                anchor -= 1
        return nums
