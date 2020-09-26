"""
1031. Maximum Sum of Two Non-Overlapping Subarrays

Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, 
which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)

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



"""
这一题是把提前计算好的思想运用到了极致。
Step 1: 提前计算好prefix_sum and suffix_sum;
Step 2: using the prefix_sum and suffix_sum, 提前计算好 the prefix_max_L, where prefix_max_L[i] = the max subarray sum with window size L before i, 
and do the same for suffix_max_L;
Step 3: travel the pre_sum and update M-long subarray sum and max_sum using the pre-calulated prefix_max_L and suffix_max_L.
"""
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], L: int, M: int) -> int:
        n = len(nums)
        
        # Step 1: 提前计算好prefix_sum and suffix_sum
        pre_sum = [0 for _ in range(n + 1)]
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]
        sur_sum = [0 for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            sur_sum[i-1] = sur_sum[i] + nums[i]
        
        # Step 2: using the prefix_sum and suffix_sum, 提前计算好 the prefix_max_L, 
        # where prefix_max_L[i] = the max subarray sum with window size L before i, and do the same for suffix_max_L
        prefix_max_L = [0 for _ in range(len(pre_sum))]   # prefix_max_L[i] = the max L-long-subarray-sum before i 
        for i in range(1, len(pre_sum)):
            if i >= L:
                prefix_max_L[i] = max(pre_sum[i] - pre_sum[i-L], prefix_max_L[i-1])
        suffix_max_L = [0 for _ in range(len(sur_sum))]   # max_right_L_sum[i] = the max L-long-subarray-sum after i 
        for i in range(len(sur_sum)-1, -1, -1):           # 注意不能写成for i, num in enumerate(A[::-1]), 否则坐标就不对了
            if i + L < len(sur_sum):
                suffix_max_L[i] = max(sur_sum[i] - sur_sum[i+L], suffix_max_L[i+1])
                
        # Step 3: travel the pre_sum and update M-long subarray sum and max_sum using the pre-calulated prefix_max_L and suffix_max_L
        max_sum = 0
        for i in range(len(pre_sum)):
            if i >= M:
                M_sum = pre_sum[i] - pre_sum[i-M]
                L_sum = max(prefix_max_L[i-M], suffix_max_L[i])  # prefix_max_L[i-M]为左边选L长的subarray的最大sum, max_right_L_sum[i]则是右边
                max_sum = max(max_sum, M_sum + L_sum)
        return max_sum
