254. Factor Combinations

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]


"""
solution 1: step 1. we get a list of factors first; step 2. then we do a dfs like combination sum
"""
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def get_factors():
            factors = []
            for i in range(2, n // 2 + 1):      # 注意范围是(2, n//2)
                if n % i == 0:
                    factors.append(i)
            return factors        
        
        def backtrack(curr_idx, curr_comb, curr_prod):
            if curr_prod == n:
                res.append(curr_comb.copy())
                return
            
            if curr_prod > n:       # this is important, otherwise it will be TLE
                return
            
            for next_idx in range(curr_idx, len(nums)):
                # if next_idx > 0 and nums[next_idx] == nums[next_idx - 1] and next_idx - 1 != curr_idx:
                #     continue                  # cannot have this because we can have multiple same number
                curr_comb.append(nums[next_idx])
                backtrack(next_idx, curr_comb, curr_prod * nums[next_idx])
                curr_comb.pop()        
        
        if n == 1 or n == 2:
            return []
        
        nums = get_factors()    # nums is sorted already
        res = []
        backtrack(0, [], 1)
        return res
      


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n == 1:
            return []
        
        def dfs(target, curr_num, path):
            if len(path) != 0:
                res.append(path + [target])
            
            for num in range(curr_num, int(target ** 0.5) + 1):     # 需要好好想想为什么是 int(target ** 0.5) + 1, 不知为什么这样可以避免重复
                if target % num == 0:
                    dfs(target // num, num, path + [num])
        
        res = []
        
        dfs(n, 2, [])
        
        return res
