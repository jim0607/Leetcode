"""
39. Recover Rotated Sorted Array

Given a rotated sorted array, recover it to sorted array in-place.（Ascending）

Example
Example1:
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
Example2:
[6,8,9,1,2] -> [1,2,6,8,9]

Challenge
In-place, O(1) extra space and O(n) time.
"""



"""
154 相同方法binary search找到minPos, __注意如果有重复的元素就要跟nums[end]比较__, 然后三步反转法recover
"""
class Solution:
    def recoverRotatedSortedArray(self, nums):
        if len(nums) == 1: return nums
        if nums[0] < nums[-1]: return nums
        
        min_idx = self._find_min_idx(nums)
        self._swap(nums, 0, min_idx - 1)    # 三步反转法: reverse the left part
        self._swap(nums, min_idx, len(nums) - 1)    # reverse the right part
        self._swap(nums, 0, len(nums) - 1)  # reverse for the 3rd time
        
    def _find_min_idx(self, nums):  # 注意如果有重复的元素就要跟nums[end]比较
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[end]:   # 跟nums[end]比较
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:       # in case there is duplicates, we decreament end by 1
                end -= 1
        return start if nums[start] <= nums[end] else end
    
    def _swap(self, nums, start, end):
        i, j = start, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
