"""
75. Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""


    
"""
经典的荷兰三色旗问题采用 Dijkstra's 3-way partitioning:
a[i] < pivot: exchange a[i] and a[lt] and i++, lt++;
a[i] > pivot: exchange a[i] and a[gt] and gt--;
a[i] = pivot: i++;
QuickSort with 3-way partitioning is very fast because it is entropy optimal
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        lt, i, gt = 0, 0, lens - 1
        pivot = 1
        while i <= gt:      # 这里要特别注意
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
                lt += 1
            elif nums[i] > pivot:
                nums[gt], nums[i] = nums[i], nums[gt]
                # i += 1 注意这里不要做i++操作
                gt -= 1
            else:
                i += 1
    
"""
同向双指针: step 1: move all 0s to the left; step 2: move all 1s to the left of the rest of the arr
这种分区的题目都可以用同向双指针
""" 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # step 1: move all 0s to the left
        anchor = 0          # anchor keeps all the 0 on its left
        for curr in range(len(nums)):
            if nums[curr] == 0:
                nums[anchor], nums[curr] = nums[curr], nums[anchor]
                anchor += 1
        
        # step 2: move all 1s to the left of the rest of the arr
        for curr in range(anchor, len(nums)):   # now anchor keeps all the 1 on its left
            if nums[curr] == 1:
                nums[anchor], nums[curr] = nums[curr], nums[anchor]
                anchor += 1
    
    
    
    
    
"""solution 3: partition twice"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.partition1(nums, 0, len(nums) - 1)
        self.partition2(nums, 0, len(nums) - 1)
        
    def partition1(self, nums, start, end):
        if start >= end:
            return
        
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] == 0:
                left += 1
            while left < right and nums[right] != 0:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
           
    def partition2(self, nums, start, end):
        if start >= end:
            return
        
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] != 2:
                left += 1
            while left < right and nums[right] == 2:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1            
