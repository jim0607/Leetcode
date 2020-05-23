16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


"""套用3sum的模板：for循环nums[i], 双指针解决twoSum问题"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        lens = len(nums)
        closestSum = nums[0] + nums[1] + nums[2]
        for i in range(lens - 2):
            left, right = i + 1, lens - 1
            while left < right:
                threeSum = nums[left] + nums[right] + nums[i]
                if abs(threeSum - target) < abs(closestSum - target):
                    closestSum = threeSum
                    
                if threeSum > target:
                    right -= 1
                elif threeSum < target:
                    left += 1
                else:
                    return target
                    
        return closestSum
