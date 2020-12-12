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
solution 1: 从每一个点开始做backtrack -  next candidate valid的条件是matrix[next_i][next_j] > matrix[curr_i][curr_j].  
O(MN*2^(MN)).  The search is repeated for each valid increasing path. TLE.
"""
class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        
        def backtrack(curr_i, curr_j, curr_lens):
            self.max_lens = max(self.max_lens, curr_lens)
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if grid[next_i][next_j] > grid[curr_i][curr_j]:
                        visited.add((next_i, next_j))
                        backtrack(next_i, next_j, curr_lens + 1)
                        visited.remove((next_i, next_j))
                        
        
        self.max_lens = 1
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                visited = set()
                visited.add((i, j))
                backtrack(i, j, 1)    # 以(i, j)开始backtrack
        return self.max_lens
      

       
        
        

"""
solution 2: memorization - O(MN)
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

"""
solution 2: with memorization to memorize the LIP from (curr_i, curr_j)
"""
class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        
        def backtrack(curr_i, curr_j):
            if (curr_i, curr_j) in memo:        # step 1: check if curr_state in memo
                return memo[(curr_i, curr_j)]
            
            LIP = 1                             # step 2: recurssively get the result for curr_state
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if grid[next_i][next_j] > grid[curr_i][curr_j]:
                        LIP = max(LIP , backtrack(next_i, next_j) + 1)
                        
            memo[(curr_i, curr_j)] = LIP        # step 3: update memo[curr_state]
            return LIP
                        
        
        memo = defaultdict(int) # ((curr_i, curr_j) --> LIP starting from (curr_i curr_j))
        m, n = len(grid), len(grid[0])
        max_lens = 1
        for i in range(m):
            for j in range(n):
                max_lens = max(max_lens, backtrack(i, j))
        return max_lens
