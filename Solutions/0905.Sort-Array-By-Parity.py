#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (73.29%)
# Likes:    687
# Dislikes: 67
# Total Accepted:    152.8K
# Total Submissions: 208.1K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array A of non-negative integers, return an array consisting of all
# the even elements of A, followed by all the odd elements of A.
# 
# You may return any answer array that satisfies this condition.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
# 
# 
# 
#


"""同向双指针 two pointers: anchor, curr"""
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        anchor, curr = 0, 0
        lens = len(A)
        
        while curr < lens:
            if A[curr] % 2 == 0:
                A[anchor], A[curr] = A[curr], A[anchor]
                curr += 1
                anchor += 1
            else:
                curr += 1
                
        return A


"""用双指针的方法做partition，与lintcode 31的方法一模一样"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        self.quickSort(A, 0, len(A) - 1)
        return A
        
    def quickSort(self, A, start, end):
        if start >= end:
            return
        
        left, right = start, end
        while left <= right:
            while left <= right and A[left] % 2 == 0:
                left += 1
            while left <= right and A[right] % 2 == 1:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
