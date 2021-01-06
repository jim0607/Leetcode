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
可以选空地trigger a bfs，选择空地的地方很好想，但是我们选择building的地方trigger a bfs会节省一些时间。
"""
"""
Use reachable_cnt[i][j] to record how many times a 0 grid has been reached 
and use dist[][] to record the sum of distance from all 1 grids to this 0 grid. 
Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a BFS. 
in the bfs, we do level bfs and update the reachable_cnt matrix and dist matrix. 遇到obstacle不放进q就可以了. 
each bfs, all position are visited, so O(MNk) where k is how many building are there or how many bfs are triggered. 
Finnaly return the min of dist[i][j] if reachable_cnt[i][j] = total number of buildings. 
Strong Prune: if starting from building (i, j), can reach all other building? 
if not, that means at least one building is isolated and can not be reached, then return -1 directly: 
in each BFS we use reachableBuildings to count how many 1s we reached. If reachableBuldings != totalBuildings - 1,
then we know not all 1s are connected are we can return -1 immediately, which greatly improved speed.
"""
class Solution:
    EMPTY = 0
    BUILDING = 1
    OBSTACLE = 2
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # 算出matrix里有多少个buildings
        total_buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.BUILDING:
                    total_buildings += 1
                    
        # trigger a bfs at each bulding, in bfs, update reachable_cnt and dist
        # rechable_cnt records how many buildings can each EMPTY reach
        # dist records what is the distance from each EMPTY to all buildings
        reachable_cnt = [[0 for _ in range(n)] for _ in range(m)]
        dist = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.BUILDING:
                    if not self._bfs(grid, i, j, total_buildings, reachable_cnt, dist): # if starting from building (i, j), can reach all other buildings?
                        return -1     # if not, that means at least one building is isolated and can not be reached - STRONG PRUNING
                 
        # get the mid_dist from dist matrix and reachable matrix
        min_dist = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.EMPTY and reachable_cnt[i][j] == total_buildings: # only EMPTY that can reach all buildings count
                    min_dist = min(min_dist, dist[i][j])
                    
        return min_dist if min_dist != float("inf") else -1
    
    def _bfs(self, grid, i, j, total_buildings, reachable_cnt, dist):
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        q.append((i, j))
        visited.add((i, j))
        
        steps = 0
        can_reach_buldings = 0      # record how many buldings can be reached from BUILDING (i, j)
        while len(q) > 0:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr_i, curr_j = q.popleft()
                for delta_i, delta_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < m and 0 <= next_j < n:
                        if (next_i, next_j) not in visited:
                            if grid[next_i][next_j] == self.BUILDING:
                                can_reach_buldings += 1     
                                visited.add((next_i, next_j))   # **** 注意这里要将(next_i, next_j) add到visited中, 但不要append到q中
                                                                # 这是因为each 1 marks a building which you cannot pass through.
                            elif grid[next_i][next_j] == self.EMPTY:
                                reachable_cnt[next_i][next_j] += 1      # update reachable_cnt
                                dist[next_i][next_j] += steps           # update dist
                                q.append((next_i, next_j))
                                visited.add((next_i, next_j))
                                
        return can_reach_buldings == total_buildings - 1    # STRONG PRUNING: if some bulding can not be reached from bulding (i, j), then return -1
    
    
    
    
    
    
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def bfs(i, j):
            q = deque()
            visited = set()
            q.append((i, j))
            visited.add((i, j))
            
            steps = -1
            while len(q) > 0:
                steps += 1
                lens = len(q)
                for _ in range(lens):
                    curr_i, curr_j = q.popleft()
            
                    if grid[curr_i][curr_j] == 1:
                        self.reach_cnt += 1
                        self.dist += steps

                    if grid[curr_i][curr_j] == 0:
                        for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            next_i, next_j = curr_i + delta_i, curr_j + delta_j
                            if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] != 2:
                                if (next_i, next_j) not in visited:
                                    q.append((next_i, next_j))
                                    visited.add((next_i, next_j))
        
        
        m, n = len(grid), len(grid[0])
        min_dist = sys.maxsize
        total_building = sum([grid[i][j] for i in range(m) for j in range(n) if grid[i][j] == 1])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.reach_cnt = 0
                    self.dist = 0
                    bfs(i, j)
                    if self.reach_cnt == total_building:
                        min_dist = min(min_dist, self.dist)
        return min_dist if min_dist != sys.maxsize else -1
