Given n items with size nums[i] which an integer array and all positive numbers. An integer target denotes the size of a backpack. Find the number of possible fill the backpack.

Each item may only be used once

Example
Given candidate items [1,2,3,3,7] and target 7,

A solution set is: 
[7]
[1, 3, 3]


"""f[i][m]=前i个物品能拼出重量m有多少种方式
f[i][m] = f[i-1][m] + f[i-1][m-A[i-1]]
f[0][0] = 1
f[0][m] = 0
f[i][0] = 1
return f[lens][M]"""
class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        lens = len(nums)
        dp = [[0] * (target + 1) for _ in range(lens + 1)]
        
        for i in range(lens + 1):
            dp[i][0] = 1
            
            if i == 0:
                for m in range(1, target + 1):
                    dp[i][m] = 0
                    
                continue
            
            for m in range(1, target + 1):
                if m >= nums[i - 1]:
                    dp[i][m] = dp[i - 1][m] + dp[i - 1][m - nums[i - 1]]
                else:
                    dp[i][m] = dp[i -1][m]
                    
        return dp[lens][target]
        
        
        
"""空间优化：滚动数组"""
class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        lens = len(nums)
        dp = [[0] * (target + 1) for _ in range(2)]
        
        for i in range(lens + 1):
            dp[i % 2][0] = 1
            
            if i == 0:
                for m in range(1, target + 1):
                    dp[i][m] = 0
                    
                continue
            
            for m in range(1, target + 1):
                if m >= nums[i - 1]:
                    dp[i % 2][m] = dp[(i - 1) % 2][m] + dp[(i - 1) % 2][m - nums[i - 1]]
                else:
                    dp[i % 2][m] = dp[(i -1) % 2][m]
                    
        return dp[lens % 2][target]
