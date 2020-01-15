#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (24.40%)
# Likes:    939
# Dislikes: 1305
# Total Accepted:    94.8K
# Total Submissions: 388.1K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# Given a list of non-negative numbers and a target integer k, write a function
# to check if the array has a continuous subarray of size at least 2 that sums
# up to a multiple of k, that is, sums up to n*k where n is also an
# integer.
# 
# 
# 
# Example 1:
# 
# 
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to
# 6.
# 
# 
# Example 2:
# 
# 
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and
# sums up to 42.
# 
# 
# 
# 
# Note:
# 
# 
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit
# integer.
# 
# 
#

# @lc code=start
"""solution 3: prefixSum + hashmap"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lens = len(nums)
        if lens < 2:
            return False
        
        prefixSumMap = {0: -1} # key: prefixSum[j], val: j/position, initial position should be -1
        prefixSum_j = 0
        for j in range(lens):
            prefixSum_j += nums[j]
            
            if k == 0:
                if prefixSum_j in prefixSumMap and j > prefixSumMap[prefixSum_j] + 1:
                    return True
            else:
                prefixSum_j = prefixSum_j % k       # (a+(n*x))%x is same as (a%x)
                if prefixSum_j in prefixSumMap and j > prefixSumMap[prefixSum_j] + 1:
                    return True

            if prefixSum_j not in prefixSumMap:
                prefixSumMap[prefixSum_j] = j
        
        return False

# @lc code=end


"""
"""solution 1: brutal force: O(N^3), O(1)"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lens = len(nums)
        if lens < 2:
            return False
        
        for j in range(1, lens + 1):
            for i in range(j - 1):
                if k == 0:
                    if sum(nums[i:j]) == 0:
                        return True
                else:
                    if sum(nums[i:j+1]) % k == 0:
                        return True
        return False"""

 

# @lc code=start
"""solution 2: prefixSum"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lens = len(nums)
        if lens < 2:
            return False
        
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
        
        for j in range(1, len(prefixSum) - 1):
            for i in range(j):
                subArrSum = prefixSum[j+1] - prefixSum[i]   # (i~j包括i,j)的subArr的subArrSum是prefixSum[j+1] - prefixSum[i]
                if k == 0:
                    if subArrSum == 0:
                        return True
                else:
                    if subArrSum % k  == 0:
                        return True 
        
        return False


