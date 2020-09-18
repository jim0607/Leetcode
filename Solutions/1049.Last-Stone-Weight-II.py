"""
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.
"""



"""
每次碰撞，我们都会减去小数乘以2， eg: 3 <--> 5, 最后变成2, 相当于3减去了3, 5也减去了3.
所以我们的目的是选一组数出来，让2*（sum_of_这些数）尽可能接近sum(nums).
也就是找一组数使他们的和尽可能接近sum(nums)//2.
由于一个数只能用一次，所以我们使用二维dp: dp[i][m] = can we use first i nums to add up to m? 
dp[i][m] = True of dp[i-1][m] == True or dp[i-1][m-A[i]] == True
"""
class Solution:
    def lastStoneWeightII(self, nums: List[int]) -> int:
        target = sum(nums) // 2
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        
        for i in range(1, len(nums) + 1):
            for m in range(1, target + 1):
                dp[i][m] = dp[i-1][m]
                if m >= nums[i-1]:      # 注意有buffer layer, 所以要比较nums[i-1]
                    dp[i][m] = dp[i][m] or dp[i-1][m-nums[i-1]]
        
        # now loop over dp to find the largest m for dp[-1][m] == True
        for m in range(target, -1, -1):
            if dp[-1][m]:
                return sum(nums) - 2*m
