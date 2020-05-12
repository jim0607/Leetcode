#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (46.62%)
# Likes:    638
# Dislikes: 67
# Total Accepted:    35.6K
# Total Submissions: 76.5K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
# 
# 
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# 
# 
# 
# 
#

class Solution:
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        # 如果本来就没有FRESH的，就直接返回0
        found = False
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.FRESH:
                    found = True
                    
        if not found:
            return 0  
        
        visited = set()
        minites = self.bfs(grid, visited)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.FRESH:
                    return -1
        
        return minites
    
    def bfs(self, grid, visited):
        """bfs to reach the fresh ones and change them into rotten ones, return the minites to reach all fresh ones"""
        
        # 1. append the rotten ones to the first level, 由于需要做层序遍历，所以要想将所有的ROTTEN都放进q （作为第一层），然后再开始q的遍历
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.ROTTEN:
                    q.append((i, j))
                    visited.add((i, j))     # 一对孪生兄弟
        
        # 2. bfs
        minites = -1        # 需要分层遍历，所以需要加入一个参数minutes
        while q:
            minites += 1
            lens = len(q)
            for _ in range(lens):   # 一层一层的来
                (x, y) = q.popleft()
                for delta_x, delta_y in self.MOVES:
                    neighbor_x, neighbor_y = x + delta_x, y + delta_y
                    if self.inBound(grid, neighbor_x, neighbor_y) and \
                    grid[neighbor_x][neighbor_y] == self.FRESH and \
                    (neighbor_x, neighbor_y) not in visited:
                        grid[neighbor_x][neighbor_y] = self.ROTTEN
                        q.append((neighbor_x, neighbor_y))
                        visited.add((neighbor_x, neighbor_y))       # 一对孪生兄弟

        return minites
                        
    def inBound(self, grid, x, y):
        m, n = len(grid), len(grid[0])
        if 0 <= x < m and 0 <= y < n:
            return True
        
        return False
