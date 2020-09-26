#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#
# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (47.30%)
# Likes:    545
# Dislikes: 50
# Total Accepted:    22.8K
# Total Submissions: 48.1K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# Given an array A of integers, return the number of (contiguous, non-empty)
# subarrays that have a sum divisible by K.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
# 
# 
#

# @lc code=start
"""
subarray sum的问题都要往prefix sum方面去想  O(N), O(N)
"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        pre_sum_dict = collections.defaultdict(int)     # pre_sum --> how many time pre_sum occured
        pre_sum_dict[0] = 1
        res = 0
        for i, num in enumerate(nums):
            pre_sum += num
            pre_sum = pre_sum % k       # (a-b)%x = a%x - b%x
            
            if (pre_sum - k) % k in pre_sum_dict:
                res += pre_sum_dict[(pre_sum - k) % k]
                
            pre_sum_dict[pre_sum] += 1
            
        return res



# @lc code=end


"""
# @lc code=start
"""solution 2: replace sum(A[i:j]) by using prefixSum
O(N^2), O(N)
correct but still TLE
"""
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        if not A or K == 0:
            return 0

        prefixSum = [0]
        for num in A:
            prefixSum.append(prefixSum[-1] + num)

        cnt = 0
        for j in range(len(A)):
            for i in range(j + 1):
                # # include i and j， i==j时，subArr只有一个元素，所以i是可以等于j的，这就是为什么i in range(j + 1)
                subArrSum = prefixSum[j+1] - prefixSum[i]
                if subArrSum % K == 0:
                    cnt += 1
        
        return cnt
        
# @lc code=end
"""


"""solution 1: brutal force (TLE)
O(N^3), O(1)"""
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        if not A or K == 0:
            return 0
        
        cnt = 0
        for j in range(len(A) + 1):
            for i in range(j):
                if sum(A[i:j]) % K == 0:   # O(N)
                    cnt += 1
        
        return cnt
