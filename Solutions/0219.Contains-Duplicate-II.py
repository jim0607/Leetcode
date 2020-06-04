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
O(N), O(N)
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        posDict = collections.defaultdict(list)
        for i, num in enumerate(nums):
            posDict[num].append(i)
            
        # note that the lst in the posDict is already sorted
        for num, lst in posDict.items():
            if len(lst) >= 2:
                for i in range(len(lst)-1):
                    if lst[i+1] - lst[i] <= k:
                        return True
                    
        return False


"""
sliding window: fix the sliding window to be k.  O(N), O(k)
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numSet = set()
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and j - i <= k:
                if nums[j] in numSet:
                    return True
                else:
                    numSet.add(nums[j])
                j += 1
                    
            numSet.remove(nums[i])
            
        return False
