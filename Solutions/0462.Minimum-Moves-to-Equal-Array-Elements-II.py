462. Minimum Moves to Equal Array Elements II

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

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
solution 1: find median by sorting
"""
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        lens = len(nums)
        median = nums[lens//2]
        return sum(abs(median - num) for num in nums)
        
        
"""
solution 2: find meddian by quick select(kth largest element) - O(N)
模板一个星期不看就不记得了
"""
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median = self._quick_select(nums, len(nums)//2, 0, len(nums)-1)
        return sum(abs(median - num) for num in nums)
    
    def _quick_select(self, nums, k, start, end):
        if start >= end:
            return nums[start]
        
        left, right = start, end
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -=1
        
        if right >= k:
            self._quick_select(nums, k, start, right)
        if left <= k:
            self._quick_select(nums, k, left, end)
            
        return nums[k]
