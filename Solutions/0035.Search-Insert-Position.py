Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        if lens == 0:
            return 0
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return lens
        start, end = 0, lens - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            elif nums[mid] < target:
                start = mid
        return end
