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
# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A:
            return A
        
        lens = len(A)
        i, j = 0, lens - 1
        temp = A[i]
        while i < j:
            while i < j and A[j] % 2 == 1:
                j -= 1
            A[i] = A[j]
            while i < j and A[i] % 2 == 0:
                i += 1
            A[j] = A[i]

        A[i] = temp

        return A
        
# @lc code=end

