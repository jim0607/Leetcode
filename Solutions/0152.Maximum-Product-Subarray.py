"""
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lens = len(nums)
        min_neg = [0 for _ in range(lens)]      # min_neg[i] = 以i结尾的最小负数
        max_pos = [0 for _ in range(lens)]      # max_pos[i] = 以i结尾的最大正数
        min_neg[0], max_pos[0] = nums[0], nums[0]
        for i in range(1, lens):        # 特别注意遍历不要包括初始状态
            if nums[i] >= 0:
                max_pos[i] = max(nums[i], max_pos[i-1] * nums[i])
                min_neg[i] = min(nums[i], min_neg[i-1] * nums[i])
            else:
                max_pos[i] = max(nums[i], min_neg[i-1] * nums[i])
                min_neg[i] = min(nums[i], max_pos[i-1] * nums[i])
        return max(max_pos)
