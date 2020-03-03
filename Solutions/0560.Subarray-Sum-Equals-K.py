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


"""
Solution 3: prefixSum+hashmap
用prefixSum，hashmap来存储prefixSum中出现的数字频率, O(N), O(N)"""
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumDict = {0: 1}   # key是prefixSum, val是how many times the prefixSum appears. 注意prefixSumDict需要初始化，所有prefixSum相关的参数都要初始化！！
        prefixSum, cnt = 0, 0

        # Our problem is: find how many pairs of <i,j> satisfies i < j and prefixSum[j]-prefixSum[i] == k?
        for num in nums:
            prefixSum += num     # 这里的prefixSum 相当于 prefixSum[j]，一般的prefixSum[j]都是这样写的，而不是单独开一个数组出来寸prefixSum
            if prefixSum - k in prefixSumDict:     # 等价于 if prefixSum[j+1]-prefixSum[i] == k
                cnt += prefixSumDict[prefixSum - k]        
            
            # 将prefixSum 存入prefixSumMap中
            if prefixSum not in prefixSumDict:
                prefixSumDict[prefixSum] = 1
            else:
                prefixSumDict[prefixSum] += 1
            
        return cnt


"""
Solution 2: prefixSum (TLE)
find all the subArrSum by using subArrSum(i~j) = prefixSum[j+1] - prefixSum[i]
O(N^2), O(N)"""
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 构造prefixSum[i]: the sum of all items before i
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        cnt = 0
        for j in range(len(nums)):
            for i in range(j + 1):
                # subArrSum(i~j包含i和j) = prefixSum[j+1] - prefixSum[i] 
                # i==j时，subArr只有一个元素，所以i是可以等于j的，这就是为什么i in range(j + 1)
                if prefixSum[j+1] - prefixSum[i] == k:
                    cnt += 1

        return cnt



"""
Solution 1: Brutal Force (TLE)
find all the subArrSum by using sum(nums[i:j])
O(N^3), O(1)"""
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        for j in range(len(nums) + 1):
            for i in range(j):
                subArrSum = sum(nums[i:j])
                if subArrSum == k:
                    cnt += 1

        return cnt
