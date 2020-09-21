"""
462. Minimum Moves to Equal Array Elements II

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, 
where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""


"""
solution 1: find median by sorting
"""
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = self._find_median(nums)
        return sum(abs(num - median) for num in nums)
    
    def _find_median(self, nums):
        nums.sort()
        return nums[len(nums)//2]
        
        
"""
solution 2: find meddian by quick select(kth largest element) - O(N)
模板一个星期不看就不记得了
"""
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = self._find_median(nums)
        return sum(abs(num - median) for num in nums)
    
    def _find_median(self, nums):
        return self._quick_select(nums, 0, len(nums) - 1, len(nums) // 2)
        
    def _quick_select(self, nums, start, end, k):
        if start >= end:
            return nums[k]
        
        pivot = nums[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if k <= right:
            return self._quick_select(nums, start, right, k)
        elif k >= left:
            return self._quick_select(nums, left, end, k)
        
        return nums[k]
