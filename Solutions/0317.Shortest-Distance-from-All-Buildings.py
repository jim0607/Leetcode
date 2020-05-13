#
# @lc app=leetcode id=317 lang=python3
#
# [317] Shortest Distance from All Buildings
#
# https://leetcode.com/problems/shortest-distance-from-all-buildings/description/
#
# algorithms
# Hard (39.68%)
# Likes:    606
# Dislikes: 34
# Total Accepted:    54.1K
# Total Submissions: 136.2K
# Testcase Example:  '[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]'
#
# You want to build a house on an empty land which reaches all buildings in the
# shortest amount of distance. You can only move up, down, left and right. You
# are given a 2D grid of values 0, 1 or 2, where:
# 
# 
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# 
# 
# Example:
# 
# 
# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# 
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# 
# Output: 7 
# 
# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at
# (0,2),
# ⁠            the point (1,2) is an ideal empty land to build a house, as the
# total 
# travel distance of 3+3+1=7 is minimal. So return 7.
# 
# Note:
# There will be at least one building. If it is not possible to build such
# house according to the above rules, return -1.
# 
#
"""
很重要的一题：
可以选空地践行bfs (也可以选1的地方)，选择0的地方很好想，但是我们选择1的地方会节省一些时间。
"""
class Solution:
    
    EMPTY = 0
    BUILDING = 1
    OBSTACLE = 2
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # find the total buldings need to reach
        self.totalBuildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.BUILDING:
                    self.totalBuildings += 1
                    
        self.reachable_cnt = [[0 for _ in range(n)] for _ in range(m)]      # how many buildings can an empty reach
        self.dist = [[0 for _ in range(n)] for _ in range(m)]               # what is the distance to all buildings for an empty
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.BUILDING:     # Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a BFS
                    allReachable = self.bfs(grid, i, j)
                    if not allReachable:        # if starting from building (i, j), can reach all other building? if not, that means at least one building is isolated and can not be reached - STRONG PRUNING
                        return -1
              
        minDist = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.EMPTY and self.reachable_cnt[i][j] == self.totalBuildings:
                    minDist = min(minDist, self.dist[i][j])
                    
        return minDist if minDist != float("inf") else -1
    
    def bfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        
        q = collections.deque()
        visited = set()
        q.append((i, j))
        visited.add((i, j))
        
        level = 0
        reachable = 0
        while q:
            level += 1
            lens = len(q)
            
            for _ in range(lens):
                curr_x, curr_y = q.popleft()
                
                for delta_x, delta_y in self.MOVES:
                    next_x, next_y = curr_x + delta_x, curr_y + delta_y
                    
                    if 0 <= next_x < m and 0 <= next_y < n and \
                    grid[next_x][next_y] == self.EMPTY and \
                    (next_x, next_y) not in visited:
                        self.reachable_cnt[next_x][next_y] += 1
                        self.dist[next_x][next_y] += level
                        q.append((next_x, next_y))
                        visited.add((next_x, next_y))
                        
                    if 0 <= next_x < m and 0 <= next_y < n and \
                    grid[next_x][next_y] == self.BUILDING and \
                    (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))       # 不要q.append((neighbor_x, neighbor_y))是因为Each 1 marks a building which you cannot pass through.
                        reachable += 1
  
        return reachable == self.totalBuildings - 1     # STRONG PRUNING: if some bulding can not be reached from (i, j) bulding, then return -1 
