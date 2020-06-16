268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8


"""
solution 1: 448类似的做法，我们通过nums[i] += 1来get rid of the 0s.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            nums[i] += 1    # get rid of 0, cuz -0 = 0, which is not good for us to tell if it has been marked as negative or not
        
        # 1st pass: change num to negative 
        for num in nums:
            idx = abs(num) - 1
            if idx == n:
                continue
            nums[idx] = -abs(nums[idx])
            
        # 2nd pass: find the positive number, then the corresponding idx is the missing number
        for i, num in enumerate(nums):
            if num > 0:
                return i
            
        return n
                
                
"""
solution 2: bit manipulation 所有的idx and num都异或起来
We can harness the fact that XOR is its own inverse
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        
        return missing
        
        
"""
solution 3: add every num together and compare with n(n+1)/2
O(1)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n*(n+1)//2
        for num in nums:
            total -= num
        
        return total
        
        
Follow up: what is there are 2 missing numbers?  How can we solve within O(1)
we can calculate the sum of the 2 missing numbers using solutino 3, and also prodct of the 2 missing number,
then 用求根公式求出来就可以了
