"""
978. Longest Turbulent Subarray

A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

 

Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:

Input: [4,8,12,16]
Output: 2
Example 3:

Input: [100]
Output: 1
"""




"""
dp: keep track of the lens of current increasing subarray and lens of current decreasing subarray.
inc = dec + 1 if A[i]>A[i-1]; dec = inc + 1 if A[i]<A[i-1]
"""
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        max_lens = 1
        inc, dec = 1, 1
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                inc = dec + 1
                dec = 1         # 注意这里要初始化
            elif A[i] < A[i-1]:
                dec = inc + 1
                inc = 1
            else:
                inc = 1
                dec = 1
            max_lens = max(max_lens, inc, dec)
        return max_lens
