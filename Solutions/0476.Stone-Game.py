"""
There is a stone game.At the beginning of the game the player picks n piles of stones in a line.

The goal is to merge the stones in one pile observing the following rules:

At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.

Have you met this question in a real interview?  
Example
Example 1:

Input: [3, 4, 3]
Output: 17
Example 2:

Input: [4, 1, 1, 4]
Output: 18
Explanation:
  1. Merge second and third piles => [4, 2, 4], score = 2
  2. Merge the first two piles => [6, 4]，score = 8
  3. Merge the last two piles => [10], score = 18
"""




"""
dp[i][j]表示合并i到j的石头需要的最小代价, including i and j.
转移函数：dp[i][j]=dp[i][k]+dp[k+1][j]+sum[i][j]（i <= k =< j). 
即合并i－j的代价为合并左边部分的代价＋合并右边部分的代价＋合并左右部分的代价（即i－j所有元素的总和）。找到使dp[i][j]最小的k.
"""
class Solution:
    def stoneGame(self, A):
        # step 1: 算出i to j的和存到sums中
        n = len(A)
        sums = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            sums[i][i] = A[i]
            for j in range(i + 1, n):
                sums[i][j] = sums[i][j-1] + A[j]
        print(sums)
                
        # step 2: dp to find dp[0][len(A)-1]
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-2, -1, -1):   # 注意要逆序遍历
            for j in range(i+1, n):
                dp[i][j] = float("inf")
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + sums[i][j])
                    
        return dp[0][len(A)-1]
