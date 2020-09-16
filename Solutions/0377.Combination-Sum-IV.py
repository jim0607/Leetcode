"""
377. Combination Sum IV

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
"""


"""
不要求输出所有的combination，所以除了dfs，还有更快的方法：背包问题。
如果问题要求用i个数加在一起拼出target，那么多半是背包问题。
f[i]=how many ways to combine to number i  背包问题一定要把总承重放到状态里！！
f[i]=f[i-A1]+f[i-A2]+f[i-A3]....
f[0] = 1
return f[target]
注意和coin change II那题进行对比，我们发现for 循环的顺序是不一样的，这是因为这一题(1,3)和(3,1)都可以算到答案里, 而coin change II那题则不可以。
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1       # 注意这里初始化为1
        
        for m in range(target + 1):
            for num in nums:    # 这里会导致(1,3)可以进solution, (3,1)也可以进solution, 所以符合题意。
                if m >= num:
                    dp[m] += dp[m - num]
                    
        return dp[target]
    
    
"""
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Answer to follow up questions:
Negative numbers will cause problems. For example:
sum of 0, and we have 1 and -1. Can have {1, -1}, {1, 1, -1, -1}, etc. There would be infinite count.
That might seem like an obvious case, but consider this case: {-3, 5}. 
Doesn't seem obvious if it will cause problems, but if you simply do 5 * -3 + 3 * 5, boom there goes the computer. 
This basically means given ANY two numbers a, and b, one positive and one negative, 
you will get infinite combinations by simply adding multiple of "a" number of "b"s and "b" number of "a"s ( ! ).

This changes the problem because the DP vector will not work. 
Updating negative numbers will require information on positive numbers that might not be updated, and vice versa. 
This can only be solved using recursion (DFS), with pre-defined max recursion depth. 
When the depth is limited, we limit them max size of a the numbers count that makes up the solution, 
so we can stop the above from happening. The algorithm will be O(2^n), where n is the max recursion depth. Very cool.
"""
"""
solution 1: dfs to find all combinations
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def backtrack(curr_idx, curr_comb, curr_sum):
            if curr_sum == target:
                res.append(curr_comb.copy())
                return
            
            if curr_sum > target:
                return 
            
            for next_idx in range(len(nums)):       # (1,3)和(3,1)都可以算到答案里，所以是Permutation problem, next_idx 从0开始
                if nums[next_idx] > target:
                    continue
                curr_comb.append(nums[curr_idx])
                backtrack(next_idx, curr_comb, curr_sum + nums[next_idx])
                curr_comb.pop()
                
                
        res = []
        backtrack(0, [], 0)
        return len(res)

    
    
    
    
    

"""为什么下面这样就是错的呢
### 因为思路不对，我们每次更新的是dp[i]，所以每一个循环更新一次。总共更新n次就对了。"""
""" """
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        
        # 这样写可以就不能区分开(1,3)和(3,1)的问题，因为当coin遍历到coin=1的时候，dp[4]+=d[3]此时的dp[3]=0所以dp[4]实际上加的是0
        # 而当coin遍历到coin=3的时候，dp[4]+=d[1]，此时d[1]被更新过一次。所以真个过程dp[4]只被更新一次，不会重复更新，也就是在(1,3)和(3,1)中只取了一种情况。
        for num in nums:
            for i in range(1, target + 1):
                if i - num >= 0:
                    dp[i] += dp[i - num]
                    
        return dp[target]




class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = []
        if not nums or target <= 0:
            return len(res)
        
        self.dfs(nums, target, 0, [], res)

        return len(res)

    def dfs(self, nums: List[int], target: int, start: int, curr: List[int], res: List[List[int]]):
        if target < 0:
            return

        if target == 0:
            res.append(curr.copy())
        
        # 遍历所有已i开头的可能的curr
        for i in range(start, len(nums)):
            curr.append(nums[i])
            self.dfs(nums, target - nums[i], 0, curr, res)      # 顺序不重要（(1, 3)和(3, 1)都可以），所以让i从0开始
            curr.pop()       
        

