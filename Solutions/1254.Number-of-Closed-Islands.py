1254. Number of Closed Islands

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:


Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2



"""
dfs just like LC 200, except cnt+=1 only if the island not otuching the boundary.
"""
class Solution:
    LAND = 0
    WATER = 1
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    continue        # boundary is not valid
                if grid[i][j] == self.LAND:
                    if (i, j) not in visited:
                        self.touching_boundary = False
                        visited.add((i, j))
                        self._dfs(grid, i, j, visited)
                        if not self.touching_boundary:  # cnt+=1 only if the island not otuching the boundary
                            cnt += 1
        return cnt
    
    def _dfs(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        for delta_i, delta_j in [(1,0), (-1,0), (0,1), (0,-1)]:
            next_i, next_j = i + delta_i, j + delta_j
            if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == self.LAND:
                if next_i == 0 or next_i == m - 1 or next_j == 0 or next_j == n - 1:
                    self.touching_boundary = True       # can not return here, need to keep dfs going to update visited
                if (next_i, next_j) not in visited:
                    visited.add((next_i, next_j))
                    self._dfs(grid, next_i, next_j, visited)
