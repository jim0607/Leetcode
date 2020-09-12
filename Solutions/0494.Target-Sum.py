"""
494. Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
"""



"""
solution 1: naive dfs - O(2^n)
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(curr_idx, curr_sum):
            if curr_idx == len(nums) - 1:
                if curr_sum == target:
                    self.cnt += 1
                return
            backtrack(curr_idx + 1, curr_sum + nums[curr_idx + 1])
            backtrack(curr_idx + 1, curr_sum - nums[curr_idx + 1])
            
            
        self.cnt = 0
        backtrack(-1, 0)
        return self.cnt
    
    
        
"""
从backtrack到memorization只需要将memo dict的key定义为backtrack的arguments, val是需要return的东西。
time complexty is how many diferent keys are possible there.
solution 2: backtrack + memorization - O(n * t) where n is len(nums), t is largest sum possible.
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(curr_idx, curr_sum):
            if curr_idx == len(nums) - 1:
                if curr_sum == target:
                    return 1
                return 0
            if (curr_idx, curr_sum) in memo:
                return memo[(curr_idx, curr_sum)]
            res = 0
            res += backtrack(curr_idx + 1, curr_sum + nums[curr_idx + 1])
            res += backtrack(curr_idx + 1, curr_sum - nums[curr_idx + 1])
            memo[(curr_idx, curr_sum)] = res
            return res
        
        
        memo = collections.defaultdict(int)  
        return backtrack(-1, 0)
