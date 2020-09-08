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
与130出重复了，代码一模一样
"""
cclass Solution:
    LAND = 0
    WATER = 1
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(curr_i, curr_j):
            visited.add((curr_i, curr_j))
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if grid[next_i][next_j] == self.LAND:
                        if (next_i, next_j) not in visited:
                            dfs(next_i, next_j)        
        
        
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            if grid[i][0] == self.LAND and (i, 0) not in visited:
                dfs(i, 0)
            if grid[i][n-1] == self.LAND and (i, n-1) not in visited:
                dfs(i, n-1)
        for j in range(n):
            if grid[0][j] == self.LAND and (0, j) not in visited:
                dfs(0, j)
            if grid[m-1][j] == self.LAND and (m-1, j) not in visited:
                dfs(m-1, j)
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.LAND and (i, j) not in visited:
                    dfs(i, j)
                    cnt += 1
        return cnt
