16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


"""套用3sum的模板：for循环nums[i], 双指针解决twoSum问题"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return None
        
        nums.sort()     # 易忘
        
        closest_sum, min_diff = float("inf"), float("inf")
        lens = len(nums)
        for i in range(lens - 2):
            left, right = i + 1, lens - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if abs(threeSum - target) < min_diff:
                    min_diff = abs(threeSum - target)
                    closest_sum = threeSum
                if threeSum > target:
                    right -= 1
                else:
                    left += 1
        return closest_sum
