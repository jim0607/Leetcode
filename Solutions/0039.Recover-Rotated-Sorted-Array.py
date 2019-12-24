"""三步反转法"""
class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if not nums:
            return None
        lens = len(nums)
        if lens == 0:
            return nums[0]
            
        # Locate the minimum point using Binary Search, in case there might be duplicates
        minPos = 0
        start, end = 0, lens - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:        # in case there might be duplicates
                end -= 1
                
        if nums[end] < nums[start]:
            minPos = end
        else:
            minPos = start
        
        if minPos == 0:
            return nums
        
        # reverse the left part
        i, j = 0, minPos - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        # reverse the right part
        i, j = minPos, lens - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        # reverse for the 3rd time
        i, j = 0, lens - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        return nums
