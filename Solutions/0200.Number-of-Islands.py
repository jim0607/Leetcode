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

       
        
Solution 2: Union Find

"""
think the grid as a graph, find how may isolated components in the graph
we traversal the whole gird, whenever find a 1, we connect all the 4 adjacent 1s. 
"""
class UnionFind:
    
    def __init__(self, grid):
        self.father = collections.defaultdict(tuple)
        self.cnt = 0        # total # of isolated components in the graph
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":           # ******注意这里容易漏掉
                    self.father[(i, j)] = (i, j)   # 特别注意这里连通的是坐标而不是grid[i][j]，因为grid[i][j]都是"1", 最后就全都指向"1"了
                    self.cnt += 1
                
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
        
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt -= 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        uf = UnionFind(grid)        # instantiate a UnionFind object
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        adj_i, adj_j = i + delta_i, j + delta_j
                        if 0 <= adj_i < m and 0 <= adj_j < n and grid[adj_i][adj_j] == "1":
                            uf.union((i, j), (adj_i, adj_j))    # union method include: 1. find the root of a and b; 2. connect a and b; 3. reduce cnt
        return uf.cnt

    
 
"""
Solution 3: dfs O(N), O(N)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(curr_i, curr_j):
            for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == "1":
                    if (next_i, next_j) not in visited:
                        visited.add((next_i, next_j))
                        dfs(next_i, next_j)
                        
        
        m, n = len(grid), len(grid[0])
        visited = set()
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    cnt += 1
        return cnt

            
            
"""
Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search.
"""
class Solution:
    
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        visited = set()
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
