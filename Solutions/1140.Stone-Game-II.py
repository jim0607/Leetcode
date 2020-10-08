"""
1140. Stone Game II

Alex and Lee continue their games with piles of stones.  
There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  
The objective of the game is to end with the most stones. 

Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  
Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. 
Alex can get 2 + 4 + 4 = 10 piles in total. 
If Alex takes two piles at the beginning, then Lee can take all three piles left. 
In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
"""



"""
dp[i][j] = the max score one can get with [i:] piles and M = j.
dp[i][j] = max(sum(piles[i:]) - dp[i+x][max(j, x)] for x in range(1, min(2*j, n))
dp[i][n] = sum(piles[i:])
"""
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suf_sum = [0 for _ in range(n + 1)]     # 先构造一个suffix sum
        for i in range(n - 1, -1, -1):
            suf_sum[i] = suf_sum[i+1] + piles[i]
            
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][n] = suf_sum[i]
        
        for i in range(n, -1, -1):
            for j in range(n, 0, -1):
                for x in range(1, min(2*j, n - i) + 1):
                    dp[i][j] = max(dp[i][j], suf_sum[i] - dp[i+x][max(j, x)])
        return dp[0][1]
