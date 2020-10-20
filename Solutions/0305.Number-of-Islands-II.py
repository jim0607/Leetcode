"""
305. Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. 
We may perform an addLand operation which turns the water at position (row, col) into a land. 
Given a list of positions to operate, count the number of islands after each addLand operation. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""



# Union find
# O(4k), where k is the length of the positions

class UnionFind:
    
    def __init__(self):
        self.father = collections.defaultdict(tuple)
        self.cnt = 0
        
    def add(self, x):
        self.father[x] = x
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
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind()
        
        res = []
        for i, j in positions:
            if (i, j) in uf.father:
                res.append(uf.cnt)  # pos already in father, meaning it's been connected, append the cnt to res
                continue

            uf.add((i, j))  # if pos not in father, then we should add it to father first, note that cnt++ at this time

            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:         # connect neighbors
                adj_i, adj_j = i + delta_i, j + delta_j
                if (adj_i, adj_j) in uf.father:
                    uf.union((i, j), (adj_i, adj_j))   # note that cnt -= 1 here, because there is one less isolated islands after connection

            res.append(uf.cnt)
                
        return res
