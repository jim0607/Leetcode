#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (51.40%)
# Likes:    2814
# Dislikes: 208
# Total Accepted:    505.3K
# Total Submissions: 974.9K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#
"""use quick select method
Python quick select (use partition) average time O(N) and worst O(N^2)"""
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return
        
        lens = len(nums)
        return self._quickSelect_(nums, 0, lens - 1, k)

    def _quickSelect_(self, nums, start, end, k):
        if start >= end:
            return nums[start]
        
        pivot_pos = self._partition_(nums, start, end)
        if k - 1 < pivot_pos:
            return self._quickSelect_(nums, start, pivot_pos - 1, k)
        elif k - 1 > pivot_pos: 
            return self._quickSelect_(nums, pivot_pos + 1, end, k)
        else:
            return nums[pivot_pos]
        
    # return the position of pivot, where on the left, all larger than pivot value, on the right, all lesser
    def _partition_(self, nums, i, j):
        pivot = nums[i]

        while i < j:
            while i < j and nums[j] < pivot:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] >= pivot:
                i += 1
            nums[j] = nums[i]

        nums[i] = pivot

        return i

# @lc code=end

