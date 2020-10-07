"""
941. Valid Mountain Array

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
"""


"""
题目要求只要有arr[i]==arr[i-1]的情况就return False, 所以不能用binary search的
"""
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        
        should_increase = True
        dec_cnt = 0
        inc_cnt = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                if not should_increase:
                    return False
                inc_cnt += 1
            elif arr[i] < arr[i-1]:
                if should_increase:
                    if dec_cnt == 0:
                        dec_cnt += 1
                        should_increase = False                        
            else:
                return False
        return dec_cnt > 0 and inc_cnt > 0
