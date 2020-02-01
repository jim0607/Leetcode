55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


"""O(N^2), O(N)"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)    # 确定状态：dp[j]表示能不能跳到位置j
        dp[0] = True                # 初始条件
        for j in range(1, len(nums)):
            for i in range(j):
                if dp[i] and i + nums[i] >= j:  # 转移方程
                    dp[j] = True
                    break
        
        return dp[-1]
    
"""TLE, should try Greedy solution with O(N), O(1)"""
