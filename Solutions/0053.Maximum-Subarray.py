#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (45.26%)
# Likes:    6000
# Dislikes: 250
# Total Accepted:    737.6K
# Total Submissions: 1.6M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
"""使用前缀和的方法，计算每个位置为结尾的subarray的最大值是多少"""
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # prefixSum记录前i个数的和，maxSum记录全局最大的值，minSum记录前i个数中的最小prefixSum
        prefixSum = 0
        minSum = 0      # 只能定义为0，因为初始的prefixSum是0
        maxSum = -float("inf")
        for num in nums:
            prefixSum += num
            maxSum = max(maxSum, prefixSum - minSum)
            minSum = min(minSum, prefixSum)

        return maxSum
        
# @lc code=end

