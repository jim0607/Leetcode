"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        candidate = sys.maxsize
        for num in nums:
            if num == candidate:
                cnt += 1
            else:
                if cnt == 0:
                    candidate = num
                    cnt = 1
                else:
                    cnt -= 1
        return candidate
