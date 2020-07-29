643. Maximum Average Subarray I

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        lens = len(nums)
        if lens == 0:
            return 0
        
        windowSum = sum(nums[:k])
        if lens <= k:
            return windowSum / k
        
        maxSum = windowSum
        for i in range(lens - k):
            windowSum = windowSum - nums[i] + nums[i + k]
            maxSum = max(maxSum, windowSum)

        return maxSum / k
