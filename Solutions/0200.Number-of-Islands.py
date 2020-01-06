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
# @lc code=start
class Solution:
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1

        return islands
    
    def bfs(self, grid, x, y, visited):
        q = collections.deque()
        q.append((x, y))
        visited.add((x, y))  # visited最好与append同事出现，像一对孪生兄弟
        while q:
            (x, y) = q.popleft()
            # 这一步相当于之前图里面的for neighbor in neighbors
            for delta_x, delta_y in self.MOVES:
                next_x = x + delta_x
                next_y = y + delta_y
                if self.isBound(next_x, next_y, grid) and grid[next_x][next_y] == "1" and (next_x, next_y) not in visited:
                    q.append((next_x, next_y))
                    visited.add((next_x, next_y))  # visited最好与append同事出现，像一对孪生兄弟

    def isBound(self, x, y, grid):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return True
        return False

        
# @lc code=end

