152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lens = len(nums)
        maxDP = [0] * lens      # 记录最大的正数
        minDP = [0] * lens      # 记录最小的负数
        maxDP[0], minDP[0] = nums[0], nums[0]
        for i in range(1, lens):    # 特别注意遍历不要包括初始状态
            if nums[i] >= 0:
                maxDP[i] = max(nums[i], maxDP[i - 1] * nums[i])
                minDP[i] = min(nums[i], minDP[i - 1] * nums[i])
                
            else:
                maxDP[i] = max(nums[i], minDP[i - 1] * nums[i])
                minDP[i] = min(nums[i], maxDP[i - 1] * nums[i])
                
        return max(maxDP)
