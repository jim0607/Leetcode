You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.


"""
dp[i][m] = how many ways to add up to m using i dices. - 背包问题总承重要放入状态
dp[i][m] += sum(dp[i-1][m - all_possible_f])
"""
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        
        
        for m in range(1, target + 1):  # 去他妈的检查了一个小时，原来就是这里错写成了range(target+1)
            if m <= f:                  # 初始化条件，只有1个骰子的时候，1->f的方法均只有1种
                dp[1][m] = 1
            
        for i in range(1, d + 1):
            for m in range(1, target + 1):
                dp[i][m] += sum(dp[i-1][m - possible_f] % MOD for possible_f in range(1, f + 1) if m >= possible_f) % MOD
                
        return dp[d][target]
