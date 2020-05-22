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
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubSum = nums[0]
        prefixSum = 0       # 一般都是初始化为0
        minPrefixSum = 0    # # 只能定义为0，因为初始的prefixSum是0
        for num in nums:
            prefixSum += num
            maxSubSum = max(maxSubSum, prefixSum - minPrefixSum)  # 注意不能更换maxSubSum和minPrefixSum的更新顺序， 比如输入为[-1]
            minPrefixSum = min(minPrefixSum, prefixSum)

        return maxSubSum
