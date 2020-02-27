#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (44.09%)
# Likes:    3786
# Dislikes: 137
# Total Accepted:    509.1K
# Total Submissions: 1.2M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#

"""
Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search.
"""
class Solution:
    
    MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):      # 矩阵的BFS必然先来两个for循环，遍历所有的节点，然后选某些节点作为起点做BFS
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    cnt += 1
                    
        return cnt
    
    def bfs(self, grid, x, y, visited):
        """bfs to find all the possible neighbors and put them into visited"""
        
        q = collections.deque()
        q.append((x, y))
        visited.add((x, y))     # visited最好与append同时出现，像一对孪生兄弟
        
        while q:
            (x, y) = q.popleft()
            for delta_x, delta_y in self.MOVES:     # 这一步相当于之前图里面的for neighbor in neighbors
                neighbor_x, neighbor_y = x + delta_x, y + delta_y
                if self.inBound(grid, neighbor_x, neighbor_y) and grid[neighbor_x][neighbor_y] == "1" and (neighbor_x, neighbor_y) not in visited:
                    q.append((neighbor_x, neighbor_y))
                    visited.add((neighbor_x, neighbor_y))       # visited最好与append同事出现，像一对孪生兄弟
                    
    def inBound(self, grid, x, y):
        m, n = len(grid), len(grid[0])
        if 0 <= x < m and 0 <= y < n:
            return True
        else:
            return False
