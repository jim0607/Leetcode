1043. Partition Array for Maximum Sum

Given an integer array A, you partition the array into (contiguous) subarrays of length at most K.  After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

 

Example 1:

Input: A = [1,15,7,9,2,5,10], K = 3
Output: 84
Explanation: A becomes [15,15,15,9,10,10,10]



"""
The subproblem is:
Suppose you are at position X of the array
What is the maximum possible sum to this point?
so we go back K-1 steps, we choose the maximum from the following combinations:
dp_sum[X - 1] + max(A[X])*1
dp_sum[X - 2] + max(A[X-1], A[X])*2
dp_sum[X - 3] + max(A[X-2], A[X-1], A[X])*3
dp_sum[X - (k-1)] + max(A[X-(k-2)] ..... A[X])*(k-1)
"""
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0 for j in range(len(A) + 1)]     # dp[j] is the maxsum before j
        for j in range(1, len(A) + 1):
            curr_max = A[j - 1]
            for i in range(min(j, K)):       # i 是后退的步数
                curr_max = max(curr_max, A[j - i - 1])
                dp[j] = max(dp[j], dp[j - i - 1] + curr_max * (i + 1))
        return dp[-1]
