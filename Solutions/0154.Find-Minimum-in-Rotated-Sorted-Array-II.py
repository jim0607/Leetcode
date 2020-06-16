Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?


"""The problem is a follow-up to the problem of 153. Find Minimum in Rotated Sorted Array. The difference is that in this problem the array can contain duplicates. 
So the question is "Would allow duplicates affect the run-time complexity? How and why?"""
"""画个图就清晰了，it should be noted that end is always on th right of minimum, and low is always on the left of minimum"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lens = len(nums)

        start, end = 0, lens - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            elif nums[mid] == nums[end]:  # 注意这里是不能drop掉一半的地方，所以如果nums里面有很多相等的数，eg: nums=[2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2..........],那每次都是讲end往后挪一位，而不是二分法希望的drop half,所以in extreme case, 时间复杂度是O(N)
                end -= 1
        
        return min(nums[start], nums[end])
        
"""Time complexity: on average (logN) where N is the length of the array, since in general it is a binary search algorithm. 
However, in the worst case where the array contains identical elements (i.e. case #3 nums[mid]==nums[end]), 
the algorithm would deteriorate to iterating each element, as a result, the time complexity becomes O(N)."""

"""第二个注意的点是这里使用nums[mid]和nums[end]做比较，尝试过多次用拿nums[start]作比较都不work,原因不知。"""
