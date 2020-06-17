219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false



"""
solution 1: hash set to store the positions where the same num appears
O(N), O(M), where N is the number of num in nums, M is the number of distinct num in nums
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        posDict = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if num in posDict:
                if i - posDict[num] <= k:
                    return True
            posDict[num] = i
            
        return False


"""
sliding window: fix the sliding window to be k.  O(N), O(k), where k is the size of the window
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numSet = set()
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and j - i <= k:
                if nums[j] in numSet:
                    return True
                numSet.add(nums[j])
                j += 1
            
            numSet.remove(nums[i])
                
        return False
