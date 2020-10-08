"""
Find the longest snake in a matrix. A snake is an increasing sequence in increments by 1.
"""



"""
特别注意：
一般四个方向都可以走的情况不能用bottom up dp. 因为dp[i][j]需要用到dp[i-1][j], 而dp[i-1][j]也需要用到dp[i][j]，
所以会形成环，DP需要无后效性，基本上是有向无环图，也就是必须能够拓扑排序。
"""
"""
正确解法: dfs + memo, same as 329. Longest Increasing Path in a Matrix
dfs with memorization to memorize the LIP from (curr_i, curr_j)
"""
class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        def backtrack(curr_i, curr_j):
            if (curr_i, curr_j) in memo:        # step 1: check if curr_state in memo
                return memo[(curr_i, curr_j)]
            
            LIP = 1                             # step 2: recurssively update memo[curr_state]
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if grid[next_i][next_j] == 1 + grid[curr_i][curr_j]:    # 唯一不同点就在这里: 329是 grid[next_i][next_j] > grid[curr_i][curr_j]
                        LIP = max(LIP , backtrack(next_i, next_j) + 1)
                        
            memo[(curr_i, curr_j)] = LIP        # step 3: update memo[curr_state]
            return LIP
                        
        
        memo = collections.defaultdict(int) # ((curr_i, curr_j) --> LIP starting from (curr_i curr_j))
        m, n = len(grid), len(grid[0])
        max_lens = 1
        for i in range(m):
            for j in range(n):
                max_lens = max(max_lens, backtrack(i, j))
        return max_lens
