"""
Given n unique postive integers, number k (1<=k<=n) and target.

Find all possible k integers where their sum is target.

Have you met this question in a real interview?  
Example
Example 1:

Input: [1,2,3,4], k = 2, target = 5
Output:  [[1,4],[2,3]]
Example 2:

Input: [1,3,4,6], k = 3, target = 8
Output:  [[1,3,4]]
"""


""" 要求输出所有组合，只能用 backtrack """

class Solution:
    def kSumII(self, nums, k, target):
        def backtrack(curr_idx, curr_sum, curr_comb):
            if curr_sum == target and len(curr_comb) == k:
                res.append(curr_comb.copy())
                return
            
            if curr_sum > target or len(curr_comb) >= k:
                return
            
            for next_idx in range(curr_idx + 1, len(nums)):
                if nums[next_idx] > target:
                    continue
                curr_comb.append(nums[next_idx])
                backtrack(next_idx, curr_sum + nums[next_idx], curr_comb)
                curr_comb.pop()
                
            
        res = []
        backtrack(-1, 0, [])
        return res






class Solution:
    def kSumII(self, A, k, target):
        res = []
        self.dfs(A, k, target, 0, [], res)
        return res
        
    def dfs(self, A, k, target, startIndex, curr, res):
        if k < 0 or target < 0:
            return 
        
        if k == 0 and target == 0:
            res.append(curr.copy())
            return
        
        for i in range(startIndex, len(A)):
            curr.append(A[i])
            self.dfs(A, k - 1, target - A[i], i + 1, curr, res)
            curr.pop()
