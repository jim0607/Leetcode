81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false




class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        if target == nums[0] or target == nums[-1]:
            return True
        
        # If nums[0] = nums[-1], the binary search would be very complicated,
        # so we remvoe the nums[-1] if it equals nums[0]
        while nums and nums[0] == nums[-1]:
            nums.pop()
        if not nums:
            return False
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target > nums[0]:            # 如果target在左半区间
                if nums[mid] == nums[0]:    # 单独拿出来判断
                    start += 1              # if there are lots of duplicates, then will take O(N) in worst case
                elif nums[0] < nums[mid] < target:
                    start = mid
                else:                       
                    end = mid
            else:               # 如果target在右半区间
                if nums[mid] == nums[-1]:    # 单独拿出来判断
                    end -= 1
                elif nums[-1] > nums[mid] > target:
                    end = mid
                else:
                    start = mid
                    
        return True if nums[start] == target or nums[end] == target else False
        
        
"""
Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""
"""
The time complexity will degrade to O(N) if there are lots of duplicates.
"""


""" 与nums[start], nums[end]比较也是对的 """
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        if len(nums) == 1: return nums[0] == target
        if target == nums[0]: return True
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target > nums[0]:
                if nums[mid] == nums[start]:
                    start += 1
                elif nums[start] < nums[mid] < target:
                    start = mid
                else:
                    end = mid
            else:
                if nums[mid] == nums[end]:
                    end -= 1
                elif target <= nums[mid] < nums[end]:
                    end = mid
                else:
                    start = mid
                    
        return True if nums[start] == target or nums[end] == target else False
