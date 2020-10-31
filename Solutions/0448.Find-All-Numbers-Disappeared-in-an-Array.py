"""
448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

"""
We use the sign of the index as the indicator. If one number never occur, 
we know the number corresponding to the idx will never be negative.
[4,3,1,3] -- > [-4,3,-1,-3], 2 is missing, so num[2-1] will never be changed to be negative 
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 1st pass: change numbers to be negative [4,3,1,3] --> [-4,3,-1,-3]
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
            
        # 2nd pass: find those numbers that has not been changed negative, there is not num corrsponding to their idx
        res = []
        for idx, num in enumerate(nums):
            if num > 0:
                res.append(idx + 1)
                
        return res
