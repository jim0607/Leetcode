"""
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            
            numSet.add(num)
            
        return False


"""
solution 2: bucket sort: 把num当idx使用
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) <= 1:
            return False
        
        idx = [False for _ in range(max(nums) + 1)]
        for num in nums:
            if idx[num]:
                return True
            else:
                idx[num] = True
        return False
