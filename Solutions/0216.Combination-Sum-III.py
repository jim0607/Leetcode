"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers 
from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
    
    
"""
一个数只能选一次，所以从curr_idx + 1开始
"""    
class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        def backtrack(curr_idx, curr_sum, curr_comb):
            if curr_sum == target and len(curr_comb) == k:
                res.append(curr_comb.copy())
                return
            
            if curr_sum > target or len(curr_comb) >= k:
                return
            
            for next_idx in range(curr_idx + 1, len(nums)):     # 一个数只能选一次，所以从curr_idx + 1开始
                if nums[next_idx] > target:
                    continue
                curr_comb.append(nums[next_idx])
                backtrack(next_idx, curr_sum + nums[next_idx], curr_comb)
                curr_comb.pop()
        
        
        if k <= 0 or k > 9 or target > 55 or target < 1:
            return[[]]
        
        nums = [i for i in range(1, 10)]
        res = []
        backtrack(-1, 0, [])
        return res  
    
    
    
    
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        self.res = []
        self.dfs(nums, k, n, 0, [])
        return self.res
    
    def dfs(self, nums, k, n, startIdx, curr):
        if k < 0 or n < 0:
            return
        
        if k == 0 and n == 0:
            self.res.append(curr.copy())
            return
        
        for i in range(startIdx, len(nums)):
            if nums[i] > n:
                continue
                
            curr.append(nums[i])
            self.dfs(nums, k - 1, n - nums[i], i + 1, curr)   # 不能出现重复数字，所以从i+1开始
            curr.pop()
