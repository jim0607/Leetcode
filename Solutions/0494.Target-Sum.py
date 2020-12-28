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
solution 1: naive backtrack - O(2^n)
backtrack结束条件：curr_idx == len(nums) - 1 and curr_sum == target
constraint for next_candidate: next_idx = curr_idx + 1, next_num either be added or be subtracted
arguments pass into backtrack function: curr_idx, curr_sum
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(curr_idx, curr_sum):
            if curr_idx == len(nums) - 1:
                if curr_sum == target:
                    self.res += 1
                return
            
            for next_num in [nums[curr_idx + 1], -nums[curr_idx + 1]]:
                backtrack(curr_idx + 1, curr_sum + next_num)
            
            
        self.res = 0
        backtrack(-1, 0)
        return self.res
    
    
        
"""
solution 2: recursion + memorization 
从backtrack到memorization只需要将memo dict的key定义为backtrack的arguments, val是需要return的东西。
time complexty is how many diferent keys are possible there
O(n * t) where n is len(nums), t is largest sum possible.
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(curr_idx, curr_sum):
            if curr_idx == len(nums) - 1:
                if curr_sum == target:
                    return 1
                return 0
            
            if (curr_idx, curr_sum) in memo:        # memorization与naive backtrack相比就多了这么一句，
                return memo[(curr_idx, curr_sum)]   # 就这一句把O(2^n) 变成了O(n*t)
            
            res = 0
            for next_num in [nums[curr_idx + 1], -nums[curr_idx + 1]]:
                res += backtrack(curr_idx + 1, curr_sum + next_num)
                
            memo[(curr_idx, curr_sum)] = res
            return res
            
            
        # 注意memo的定义要遵守bottom up的原则
        # (curr_idx, curr_sum) --> start from (curr_idx, curr_sum), how many ways to get to (last_idx, target)
        memo = defaultdict(int)     
        # backtrack函数返回值必须跟memo的val一致: start from (curr_idx, curr_sum), how many ways to get to (last_idx, target)
        return backtrack(-1, 0)   
