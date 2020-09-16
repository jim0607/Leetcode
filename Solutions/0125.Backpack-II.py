125. Backpack II

There are n items and a backpack with size m. Given array A representing the size of each item and array V representing the value of each item.

What's the maximum value can you put into the backpack?

A[i], V[i], n, m are all integers.
You can not split an item.
The sum size of the items you want to put into backpack can not exceed m.
Each item can only be picked up once

Example 1:

Input: m = 10, A = [2, 3, 5, 7], V = [1, 5, 2, 4]
Output: 9
Explanation: Put A[1] and A[3] into backpack, getting the maximum value V[1] + V[3] = 9


"""
https://www.kancloud.cn/kancloud/pack/70125
这是最基础的背包问题，特点是：每种物品仅有一件，可以选择放或不放。
用子问题定义状态：即f[i][v]表示前i件物品恰放入一个容量为v的背包可以获得的最大价值。
f[i][j]=max{f[i-1][j],f[i-1][j-A[i]]+V[i]}
将前i件物品（包括i）放入容量为j的背包中”这个子问题，若只考虑第i件物品的策略（放或不放），
那么就可以转化为一个只牵扯前i-1件物品的问题。如果不放第i件物品，那么问题就转化为“前i-1件物品放入容量为a的背包中”，价值为f[i-1][v]；
如果放第i件物品，那么问题就转化为“前i-1件物品放入剩下的容量为j-A[i]的背包中”，此时能获得的最大价值就是f[i-1][j-A[i]]再加上通过放入第i件物品获得的价值V[i]
"""

class Solution:
    def backPackII(self, target, A, V):
        dp = [[0 for _ in range(target + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for m in range(1, target + 1):
                dp[i][m] = dp[i-1][m]
                if m >= A[i-1]:
                    dp[i][m] = max(dp[i][m], dp[i-1][m-A[i-1]] + V[i-1])
                    
        return dp[len(A)][target]

    
    
        
        
"""
optimize space using rolling array cuz dp[i] depends only on dp[i-1]"""
class Solution:
    def backPackII(self, m, A, V):
        if not A:
            return 0
            
        lens = len(A)
        dp = [[0] * (m + 1) for _ in range(2)]

        for i in range(lens):
            
            dp[i % 2][0] = 0
            
            for j in range(1, m + 1):
                if i == 0:      # initialize
                    dp[i][j] = V[0] if A[0] <= j else 0
                    continue
                
                if A[i] <= j:
                    dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - A[i]] + V[i])
                
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j]
                
        return dp[(lens - 1) % 2][m]
