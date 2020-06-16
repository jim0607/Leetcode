A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.


"""变形的OOOXXX问题，画个图分四种情况讨论就可以判断是drop left还是drop right了"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lens = len(nums)
        if lens == 0:
            return 
        if lens == 1:
            return 0
        if nums[0] > nums[1]:  # [2，1]输出0
            return 0
        if nums[-1] > nums[-2]: # [1,2]输出1
            return lens - 1
        start, end = 1, lens - 2
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                end = mid
            elif nums[mid] < nums[mid-1] and nums[mid] > nums[mid+1]:
                end = mid
            elif nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]:
                start = mid
        if nums[end] > nums[start]:
            return end
        else:
            return start           
            
"""It should be noted that the problem says nums[i] ≠ nums[i+1], if not, it has to be O(N), 
eg: [2,2,2,2,2,2,3,2,2,2,2,2],如果nums[mid]取到的是2，那根本没办法判断是要丢掉左边还是右边，因为很可能nums[mid-1]=nums[mid]=nums[mid+1]"""
