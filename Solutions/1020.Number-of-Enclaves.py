"""
1020. Number of Enclaves

Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
Example 2:

Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.
 
Note:
1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.
"""



"""
very similar with 1254. 用一个全局变量self.is_touching_border来判断是否touching border.
"""
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(curr_i, curr_j):
            visited.add((curr_i, curr_j))
            self.cnt += 1
            if curr_i == 0 or curr_i == m - 1 or curr_j == 0 or curr_j == n - 1:
                self.touching_border = True
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == 1:
                    if (next_i, next_j) not in visited:
                        dfs(next_i, next_j)
        
        
        m, n = len(grid), len(grid[0])
        visited = set()
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    self.touching_border = False
                    self.cnt = 0
                    dfs(i, j)
                    if not self.touching_border:
                        res += self.cnt
        return res
