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
# @lc code=start
class Solution:
    EMPTY = 0
    BUILDING = 1
    WALL = 2

    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def shortestDistance(self, grid: List[List[int]]) -> int:
        # edge case check
        if not grid or not grid[0]:
            return -1
        
        rows, cols = len(grid), len(grid[0])

        # 在grid[i][j]=0的地方，有多少个1可以过来。只有所有的1都能到达这个(i, j)，这个（i， j）才有可能建房子。
        reachable_cnt = [[0 for j in range(cols)] for i in range(rows)]

        # 在grid[i][j]=0的地方，到所有1的地方的距离是多少。最后的答案是比较所有的距离选择最小的那一个。
        dist = [[0 for j in range(cols)] for i in range(rows)]

        min_dist = float("inf")

        totalBuildings = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == self.BUILDING:
                    self.bfs(grid, i, j, dist, reachable_cnt)
                    totalBuildings += 1
        
        for i in range(rows):
            for j in range(cols):
                if reachable_cnt[i][j] == totalBuildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    print(i, j)
        
        return min_dist if min_dist != float("inf") else -1

    def bfs(self, grid, x, y, dist, reachable_cnt):
        q = collections.deque()
        visited = set()
        q.append((x, y))
        visited.add((x, y))
        level = 0
        while q:
            # 需要层序遍历的BFS，因为每一个1的位置都需要找到所有的可能到达的0的位置，并记录到达那个0需要的步数/层数
            lens = len(q)
            level += 1
            for _ in range(lens):
                (x, y) = q.popleft()
                for delta_x, delta_y in self.MOVES:
                    new_x = x + delta_x
                    new_y = y + delta_y
                    if self.inBound(new_x, new_y, grid) and grid[new_x][new_y] == self.EMPTY and (new_x, new_y) not in visited:
                        visited.add((new_x, new_y)) 
                        q.append((new_x, new_y))
                        reachable_cnt[new_x][new_y] += 1  # 表示(new_x, new_y)这个位置能够到达我们选择做bfs的1的那个位置(x, y)
                        dist[new_x][new_y] += level # 表示(new_x, new_y)这个位置到达我们选择做bfs的1的那个位置(x, y)的层数/步数

    def inBound(self, x, y, grid):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return True
        return False

"""
prune: if not all 1s can be reached, return -1
Use reachable_cnt to record how many times a 0 grid has been reached and use distSum to record the sum of distance from all 1 grids to this 0 grid. 
A powerful pruning is that during the BFS we use reachableBuildings to count how many 1 grids we reached. 
If reachableBuldings != buildings - 1 then we know not all 1 grids are connected are we can return -1 immediately, which greatly improved speed.
"""
class Solution:
    EMPTY = 0
    BUILDING = 1
    WALL = 2
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        self.totalBuildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.BUILDING:
                    self.totalBuildings += 1
                
        self.reachable_cnt = [[0] * n for _ in range(m)]     # Use reachable_cnt to record how many times a 0 grid has been reached
        self.distSum = [[0] * n for _ in range(m)]       # the sum of distance from all 1 grids to this 0 grid
        
        for i in range(m):      # Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a BFS
            for j in range(n):
                if grid[i][j] == self.BUILDING:
                    allBuildingsReachable = self.bfs(grid, i, j)
                    if not allBuildingsReachable:   # if not all building could be reached from (i, j), it means some buildings are isolated.
                        return -1
        
        minDist = float("inf")
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.EMPTY and self.reachable_cnt[i][j] == self.totalBuildings:
                    minDist = min(minDist, self.distSum[i][j])
        
        return -1 if minDist == float("inf") else minDist                  
            
    def bfs(self, grid, i, j):
        q = collections.deque()
        visited = set()
        q.append((i, j))
        visited.add((i, j))
        
        steps, reachableBuildings = 0, 0
        while q:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                (x, y) = q.popleft()
                for delta_x, delta_y in self.MOVES:
                    neighbor_x, neighbor_y = x + delta_x, y + delta_y
                    
                    if self.inBound(grid, neighbor_x, neighbor_y) and (neighbor_x, neighbor_y) not in visited:
                        if grid[neighbor_x][neighbor_y] == self.EMPTY:
                            q.append((neighbor_x, neighbor_y))
                            visited.add((neighbor_x, neighbor_y))
                            self.reachable_cnt[neighbor_x][neighbor_y] += 1
                            self.distSum[neighbor_x][neighbor_y] += steps
                            
                        if grid[neighbor_x][neighbor_y] == self.BUILDING:
                            visited.add((neighbor_x, neighbor_y))   # 不用q.append((neighbor_x, neighbor_y))是因为Each 1 marks a building which you cannot pass through.
                            reachableBuildings += 1

        return reachableBuildings == self.totalBuildings - 1      # if starting from one building, can reach all other building? if not, that means at least one building is isolated and can not be reached.
    
    def inBound(self, grid, x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return True
        
        return False
