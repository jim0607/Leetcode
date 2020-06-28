329. Longest Increasing Path in a Matrix

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


"""
dfs + backtrack - next candidate valid的条件是matrix[next_i][next_j] > matrix[curr_i][curr_j].  
O(2^(MN)).  The search is repeated for each valid increasing path. TLE.
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(curr_i, curr_j, curr_lens):
            self.max_lens = max(self.max_lens, curr_lens)
            for delta_i, delta_j in moves:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and (next_i, next_j) not in visited \
                and matrix[next_i][next_j] > matrix[curr_i][curr_j]:
                    visited.add((next_i, next_j))
                    dfs(next_i, next_j, curr_lens + 1)
                    visited.remove((next_i, next_j))        # backtrack
                    
        self.max_lens = 1
        for i in range(m):
            for j in range(n):
                visited = {(i, j)}
                dfs(i, j, 1)
                
        return self.max_lens
        

"""
下面的写法也是naive dfs, 很容易理解
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(curr_i, curr_j):
            max_len = 1
            for delta_i, delta_j in moves:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and (next_i, next_j) not in visited \
                and matrix[next_i][next_j] > matrix[curr_i][curr_j]:
                    visited.add((next_i, next_j))
                    max_len = max(max_len, dfs(next_i, next_j) + 1)
                    visited.remove((next_i, next_j))        # backtrack
                    
            return max_len
                    
        max_lens = 1
        for i in range(m):
            for j in range(n):
                visited = {(i, j)}
                max_len = dfs(i, j)
                max_lens = max(max_lens, max_len)
                
        return max_lens
        
        
        

"""
由于题目并不要求算出path, 所以可以用dfs+memorization.
In computing, memoization is an optimization technique used primarily to speed up computer programs by 
storing the results of expensive function calls and returning the cached result when the same inputs occur again.
In our problem, we recursively call dfs(x, y) for many times. But if we already know all the results for the four adjacent cells, 
we only need constant time. During our search if the result for a cell is not calculated, we calculate and cache it; otherwise, we get it from the cache directly.
Time complexity : O(mn). Each vertex/cell will be calculated once and only once, and each edge will be visited once and only once. 
The total time complexity is then O(V+E). V is the total number of vertices and E is the total number of edges. 
In our problem, O(V) = O(mn), O(E) = O(4V) = O(mn).
简化一点，这题可以不用visited标记，
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(curr_i, curr_j, memo):
            if (curr_i, curr_j) in memo:
                return memo[(curr_i, curr_j)]
            
            memo[(curr_i, curr_j)] = 1      # 初始化
            for delta_i, delta_j in moves:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and matrix[next_i][next_j] > matrix[curr_i][curr_j]:
                    memo[(curr_i, curr_j)] = max(memo[(curr_i, curr_j)], dfs(next_i, next_j, memo) + 1)     # 更新memo[(curr_i, curr_j)]
                    
            return memo[(curr_i, curr_j)]
                    
        max_lens = 1
        memo = collections.defaultdict(int)    # memo[(i, j)] = LIP to reach (i, j)
        for i in range(m):
            for j in range(n):
                max_len = dfs(i, j, memo)
                max_lens = max(max_lens, max_len)
                
        return max_lens
