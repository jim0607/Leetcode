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
"""solution 3: replace sum(A[i:j]) by using prefixSum
and use hashmap to store frequency of subArrSum
O(N), O(N)
"""
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefixSumDict = {0: 1} # key is the prefixSum, val is how many times the prefixSum appears
        prefixSum = 0
        cnt = 0
        for num in A:
            prefixSum += num
            prefixSum %= K
            if prefixSum in prefixSumDict:
                cnt += prefixSumDict[prefixSum]
                prefixSumDict[prefixSum] += 1
                
            else:
                prefixSumDict[prefixSum] = 1
                
        return cnt



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
