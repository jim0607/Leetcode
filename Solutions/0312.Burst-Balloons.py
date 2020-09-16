"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. 
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
             
  
"""
dp[i][j] = max coin we can get from i to j, not including i, not including j.
dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j] for k in range(i+1, j))
dp[i][k] 的意义是什么呢，是打爆区间 (i, k) 内 (not including i, not including k) 所有的气球后的最大得分，
此时第 i+1 到 k-1 个气球已经爆掉了已经不能用了，同理，第 k+1 到 j-1 个气球也已经爆掉不能用了，
这就是说区间 (i, j) 中除了第k个气球，其他的都已经爆了，那么周围的气球只能是第 i 个，和第 j 个了，
所以得分应为 nums[i] * nums[k] * nums[j]
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(i+2, n):
                dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j] for k in range(i+1, j))
        return dp[0][n-1]
  
  
  
  
  
"""
backtrack without memorizaiton - O(2^N)
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def backtrack(curr_nums, curr_coins):
            if len(curr_nums) == 2:
                self.max_coins = max(self.max_coins, curr_coins)
                return 
            for i in range(1, len(curr_nums)-1):
                next_nums = curr_nums[:i] + curr_nums[i+1:]
                backtrack(next_nums, curr_coins + curr_nums[i-1] * curr_nums[i] * curr_nums[i+1])
                
        
        self.max_coins = 0
        backtrack([1] + nums + [1], 0)
        return self.max_coins
  
  
"""
backtrack with memorizaiton - O(N^2).
we can see that the key in memo dictionary is the state we use in the naive backtrack solution.
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def backtrack(curr_nums):
            if len(curr_nums) == 3:         # step 1. base case
                return curr_nums[1]
            
            if tuple(curr_nums) in memo:    # step 2: check if curr_state in memo
                return memo[tuple(curr_nums)]
            
            max_coins = 0                   # step 3: recurssively update memo[curr_state]
            for i in range(1, len(curr_nums)-1):
                next_nums = curr_nums[:i] + curr_nums[i+1:]
                max_coins = max(max_coins, backtrack(next_nums) + curr_nums[i-1] * curr_nums[i] * curr_nums[i+1])
                
            memo[tuple(curr_nums)] = max_coins
            return max_coins
                
        
        memo = collections.defaultdict(int)     # curr_nums-->the max_coins we can get from curr_nums
        return backtrack([1] + nums + [1])
      
      
  
             
"""
the above solution could be further simplified as using index instead of curr_nums to represent state.
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def backtrack(curr_i, curr_j):
            if curr_j == curr_i:         # step 1. base case
                return 0
            
            if (curr_i, curr_j) in memo:     # step 2: check if curr_state in memo
                return memo[(curr_i, curr_j)]
            
            max_coins = 0                   # step 3: recurssively update memo[curr_state]
            for idx in range(curr_i + 1, curr_j):
                left = backtrack(curr_i, idx)
                right = backtrack(idx, curr_j)
                
                # 因为是先burst left and right, 最后conquer, 所以conquer的时候只剩下nums[i] and nums[j], 所以是 nums[i] * nums[k] * nums[j]
                max_coins = max(max_coins, left + right + nums[curr_i] * nums[idx] * nums[curr_j])
            
            memo[(curr_i, curr_j)] = max_coins
            return max_coins
                
        
        memo = collections.defaultdict(int)     # curr_nums-->the max_coins we can get from curr_nums
        nums = [1] + nums + [1]
        return backtrack(0, len(nums)-1)
