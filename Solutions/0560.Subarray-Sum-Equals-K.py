#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.26%)
# Likes:    3018
# Dislikes: 84
# Total Accepted:    179.2K
# Total Submissions: 413.4K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Note:
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
# 
#
"""方法1 TLE：用prefixSum, O(N^2), O(N)
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 构造prefixSum[i]: the sum of all items before i
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        cnt = 0
        for j in range(len(prefixSum)):
            for i in range(j):
                if prefixSum[j] - prefixSum[i] == k:
                    cnt += 1

        return cnt"""

"""方法2：用prefixSum，hashmap来存储prefixSum中出现的数字频率, O(N), O(N)"""
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumMap = {0: 1}
        sums, cnt = 0, 0
        # Our problem is: find how many pairs of <i,j> satisfies i < j and prefixSum[j]-prefixSum[i] == k?
        for num in nums:
            sums += num     # sums 相当于 prefixSum[j]，一般的prefixSum[i]都是这样写的，而不是单独开一个数组出来寸prefixSum
            if sums - k in prefixSumMap:     # if prefixSum[j]-prefixSum[i] == k
                cnt += prefixSumMap[sums - k]        
                
            if sums in prefixSumMap:
                prefixSumMap[sums] += 1
            else:
                prefixSumMap[sums] = 1
            
            return cnt
        
