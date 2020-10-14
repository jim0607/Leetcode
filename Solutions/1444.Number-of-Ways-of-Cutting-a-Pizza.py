"""
1444. Number of Ways of Cutting a Pizza

Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell)
and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, 
then you choose a cut position at the cell boundary and cut the pizza into two pieces. 
If you cut the pizza vertically, give the left part of the pizza to a person. 
If you cut the pizza horizontally, give the upper part of the pizza to a person. 
Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. 
Since the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:

Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1
Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1
 
Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
"""



"""
since after each cut, the remaining matrix is always the down right corner of the matrix. 
dp[i][j][k] = with i rows left and j cols left, how many ways to cut it using k cuts.
It's easier to implement the bottum up solution.
memo[(i, j, k)] returns the number of ways to cut pizza[i:n][j:m] into k pieces.

Step 1: In order to fast get how many apples are there in the down-right corner pizza[i:n][j:m] block,
construct suff_sum similar with 304. Range Sum Query 2D - Immutable.
Step 2: dfs + memo.

time: O(k*m*n*(m+n)). There are total k*m*n states in dfs(...k, r, c...),
and each state needs maximum (m+n) times to cut in horizontal or vertical.
space: O(k*m*n)
"""
class Solution:
    def ways(self, pizza: List[str], K: int) -> int:
        MOD = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        
        # construct suff_sum, suff_sum[i][j] = how many apples are there 
        # in the down-right corner pizza[i:n][j:m] block
        suff_sum = [[0] * (n + 1) for _ in range(m + 1)]    
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                suff_sum[i][j] = suff_sum[i][j+1] + suff_sum[i+1][j] - suff_sum[i+1][j+1] + \
                                 (1 if pizza[i][j] == "A" else 0)
                
                
        def dfs(i, j, k):
            if suff_sum[i][j] == 0:
                return 0
            if k == 0:
                return 1
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            
            res = 0
            for next_i in range(i + 1, m):          # 如果这一刀我们选择 cut horizontally
                if suff_sum[i][j] - suff_sum[next_i][j] >= 1:   # 保证这一刀下去上半部分至少有一个苹果
                    res = (res + dfs(next_i, j, k - 1)) % MOD
            for next_j in range(j + 1, n):          # 如果这一刀我们选择 cut vertically
                if suff_sum[i][j] - suff_sum[i][next_j] >= 1:
                    res = (res + dfs(i, next_j, k - 1)) % MOD
                    
            memo[(i, j, k)] = res
            return res        
        
        
        memo = defaultdict(int)     # (i, j, k) --> # of ways
        return dfs(0, 0, K - 1)
