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
solution 1: naive dfs - O(2^n)
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.cnt = 0
        self._dfs(nums, target, 0, nums[0])
        self._dfs(nums, target, 0, -nums[0])
        return self.cnt
        
    def _dfs(self, nums, target, curr_idx, curr_sum):
        if curr_idx == len(nums) - 1:
            if curr_sum == target:
                self.cnt += 1
            return
        
        self._dfs(nums, target, curr_idx + 1, curr_sum + nums[curr_idx+1])
        self._dfs(nums, target, curr_idx + 1, curr_sum - nums[curr_idx+1])
        
"""
solution 1: 把cnt传到参数里的写法
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self._dfs(nums, target, 0, nums[0], 0) + self._dfs(nums, target, 0, -nums[0], 0)
        
    def _dfs(self, nums, target, curr_idx, curr_sum, cnt):
        if curr_idx == len(nums) - 1:
            if curr_sum == target:
                cnt += 1
            return cnt
        
        cnt_1 = self._dfs(nums, target, curr_idx + 1, curr_sum + nums[curr_idx+1], cnt)
        cnt_2 = self._dfs(nums, target, curr_idx + 1, curr_sum - nums[curr_idx+1], cnt)
        
        return cnt_1 + cnt_2
        
        
        
"""
solution 2: naive dfs + memorization - O(n * t) where n is len(nums), t is target
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = collections.defaultdict(int)     # memo[(i, t)] = 用前i个num拼出t的方式有多少种
        return self._dfs(nums, target, 0, nums[0], memo) + self._dfs(nums, target, 0, -nums[0], memo)
        
    def _dfs(self, nums, target, curr_idx, curr_sum, memo):
        if curr_idx == len(nums) - 1:
            if curr_sum == target:
                memo[(curr_idx, curr_sum)] = 1
            else:
                memo[(curr_idx, curr_sum)] = 0
        
        if (curr_idx, curr_sum) in memo:
            return memo[(curr_idx, curr_sum)]
        
        cnt_1 = self._dfs(nums, target, curr_idx + 1, curr_sum + nums[curr_idx+1], memo)
        cnt_2 = self._dfs(nums, target, curr_idx + 1, curr_sum - nums[curr_idx+1], memo)
        
        memo[(curr_idx, curr_sum)] = cnt_1 + cnt_2
        return cnt_1 + cnt_2
