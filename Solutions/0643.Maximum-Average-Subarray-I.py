"""
643. Maximum Average Subarray I

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. 
And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        max_avg = -sys.maxsize
        for i in range(len(nums)):
            window_sum += nums[i]
            if i >= k:
                window_sum -= nums[i-k]
            if i >= k - 1:
                max_avg = max(max_avg, window_sum / k)
        return max_avg
