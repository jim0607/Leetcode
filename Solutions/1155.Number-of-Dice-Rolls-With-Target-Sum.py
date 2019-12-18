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


""" dp[i][j]表示用i个骰子得出j的组合数
    dp[i][j] = dp[i-1][j-1] + ... + dp[i-1][j-f] if (j-f >= 0)  
    可以优化为1维，因为每次更新都只与上一次相关
    注意取模返回"""
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0]*(target+1) for _ in range(d+1)]
        # 初始化条件，只有1个骰子的时候，1->f的方法均只有1种
        for i in range(1, target+1):   # 去他妈的检查了一个小时，原来就是这里错写成了range(target+1)
            if i <= f:
                dp[1][i] = 1
        for i in range(1, d+1):
            for j in range(1, target+1):
                for k in range(1, min(f, j)+1):
                    dp[i][j] += dp[i-1][j-k]   # 用i-1个骰子实现j-k，然后用剩下的一个实现j-(j-k)=k
                    dp[i][j] %= (10**9+7)
        return dp[d][target]
    
# 可优化为1维，不太理解！
