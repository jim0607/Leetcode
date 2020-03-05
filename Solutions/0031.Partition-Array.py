31. Partition Array

Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Example:
Input:
[3,2,2,1],2
Output:1
Explanation:
the real array is[1,2,2,3].So return 1
Challenge：Can you partition the array in-place and in O(n)?


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        if not nums:
            return 0
        
        i, j = 0, len(nums) - 1
        temp = nums[i]  # nums[i]在后面会改变，所以需要存储起来
        while i < j:
            while i < j and nums[j] >= k:   # 都是先判断j
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] < k:
                i += 1
            nums[j] = nums[i]
            
        nums[i] = temp  # nums[i]的值需要回归，这一步是必须的！
        
        return i if nums[i] >= k else i + 1     # 不懂为什么要这样
