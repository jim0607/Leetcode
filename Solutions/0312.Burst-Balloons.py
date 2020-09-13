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
