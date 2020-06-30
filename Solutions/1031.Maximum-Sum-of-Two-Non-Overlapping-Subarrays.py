1031. Maximum Sum of Two Non-Overlapping Subarrays

Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.

Example 1:

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
Example 2:

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
Example 3:

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.



"""
Step 1: find the prefix_sum and suffix_sum;
Step 2: using the prefix_sum and suffix_sum, find the prefix_max_L, where prefix_max_L[i] = the max subarray sum with window size L before i;
do the same for prefix_max_M, suffix_sum_L, suffix_sum_M;
Step 3: travel the arr and update max_sum as max(max_sum, prefix_max_L[i] + suffix_max_M[i], prefix_max_M[i] + suffix_max_L[i])
"""
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        lens = len(A)
        prefix_sum = [0 for _ in range(lens + 1)]
        for i, num in enumerate(A):
            prefix_sum[i + 1] = prefix_sum[i] + num
        
        suffix_sum = [0 for _ in range(lens + 1)]
        for i in range(lens - 1, -1, -1):               # 注意不能写成for i, num in enumerate(A[::-1]), 否则坐标就不对了
            suffix_sum[i] = suffix_sum[i + 1] + A[i]
            
        # print(prefix_sum, suffix_sum)
            
        prefix_max_L = [0 for _ in range(lens + 1)]     # the max subarray sum with window size L before i, not including i
        prefix_max_M = [0 for _ in range(lens + 1)]     # the max subarray sum with window size M before i, not including i
        for i in range(lens):
            if i + 1 - L >= 0:
                prefix_max_L[i + 1] = max(prefix_max_L[i], prefix_sum[i + 1] - prefix_sum[i + 1 - L])
            if i + 1 - M >= 0:
                prefix_max_M[i + 1] = max(prefix_max_M[i], prefix_sum[i + 1] - prefix_sum[i + 1 - M])
                
        # print(prefix_max_L, prefix_max_M)
                
        suffix_max_L = [0 for _ in range(lens + 1)]     # the max subarray sum with window size L
        suffix_max_M = [0 for _ in range(lens + 1)]     # the max subarray sum with window size M
        for i in range(lens - 1, -1, -1):
            if i + L < lens + 1:
                suffix_max_L[i] = max(suffix_max_L[i + 1], suffix_sum[i] - suffix_sum[i + L])   # ***注意事项suffix_sum[i + L]***
            if i + M < lens + 1:
                suffix_max_M[i] = max(suffix_max_M[i + 1], suffix_sum[i] - suffix_sum[i + M])
                
        # print(suffix_max_L, suffix_max_M)
                
        max_sum = 0
        for i in range(lens + 1):
            max_sum = max(max_sum, prefix_max_L[i] + suffix_max_M[i], prefix_max_M[i] + suffix_max_L[i])
            
        return max_sum
