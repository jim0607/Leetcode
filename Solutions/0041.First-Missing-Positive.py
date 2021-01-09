"""
41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


"""
O(n), O(n)
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num > 0:
                seen.add(num)
        
        n = 1
        while n in seen:
            n += 1
        return n


"""
O(N), O(1) solution
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)   # the answer must be in range 1 to n
        # Base case.
        if 1 not in nums:
            return 1
        if n == 1:     # nums = [1]
            return 2
        
        # 1st pass: change all negtive numbers to be 1, so that there will be no negtive numbers
        # [3,4,-1,1] --> [3,4,1,1]
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # 2nd pass: change the positive numbers into negative [3,4,1,1] --> [-3,-4,1,-1]
        for num in nums:
            idx = abs(num)
            if idx == n:
                nums[0] = -abs(nums[0])
            else:
                nums[idx] = -abs(nums[idx])
                
        # 3rd pass: find the first positive number, and the corresponding idx is missing
        for idx in range(1, n):
            if nums[idx] > 0:
                return idx
            
        return n if nums[0] > 0 else n + 1
