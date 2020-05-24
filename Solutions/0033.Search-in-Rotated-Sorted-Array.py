Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4


    
    
    
# 九章算法模板真香！画个图分几个区间讨论就可以了！  
"""Approach 2: one pass approach"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        if lens == 0:
            return -1
        
        if target == nums[0]:
            return 0
        
        start, end = 0, lens - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if target >= nums[0]:
                if nums[0] <= nums[mid] < target:   # 往左逼近
                    start = mid
                else:
                    end = mid
            
            else:
                if target <= nums[mid] < nums[0]:  # 保持一致，往左逼近
                    end = mid
                else:
                    start = mid
                    
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1

    
    
    
    
    
    
    
    
"""Approach 1: Binary search
The problem is to implement a search in \mathcal{O}(\log(N))O(log(N)) time that gives an idea to use a binary search.

The algorithm is quite straightforward :

Find a rotation index rotation_index, i.e. index of the smallest element in the array. Binary search works just perfect here.

rotation_index splits array in two parts. Compare nums[0] and target to identify in which part one has to look for target.

Perform a binary search in the chosen part of the array."""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        if lens == 0:
            return -1
        [minPos, minNum] = self.findMin(nums)
        if minPos == 0:
            return self.binarySearch(nums, target)
        if target == minNum:
            return minPos
        elif target == nums[0]:
            return 0
        elif target < minNum:
            return -1
        elif minNum < target < nums[0]:
            if self.binarySearch(nums[minPos:], target) == -1:
                return -1
            else:
                return minPos + self.binarySearch(nums[minPos:], target)
        elif target > nums[0]:
            return self.binarySearch(nums[:minPos], target) 
        
    def findMin(self, nums: List[int]):
        lens = len(nums)
        if nums[0] <= nums[-1]:
            return [0, nums[0]]
        start, end = 0, lens - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= nums[0]:
                end = mid
            else:
                start = mid
        if nums[end] < nums[0]:
            return [end, nums[end]]
        if nums[start] < nums[0]:
            return [start, nums[start]]
        
    def binarySearch(self, nums: List[int], target) -> int:
        lens = len(nums)
        if lens == 0:
            return -1
        start, end = 0, lens - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1 
