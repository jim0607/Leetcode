305. Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

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




# Union find
# O(4k), where k is the length of the positions

class UnionFind:
    def __init__(self):
        self.father = collections.defaultdict()
        self.cnt = 0
        
    def add(self, x):
        self.father[x] = x
        self.cnt += 1
        
    def find(self, x):
        if self.father[x] == x:
            return x
        
        self.father[x] = self.find(self.father[x])
        
        return self.father[x]
    
    def connect(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt -= 1        
            
        
class Solution:
    
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        graph = UnionFind()        # instantiate the UnionFind class to get a graph
        
        res = []
        for pos in positions:
            pos = (pos[0], pos[1])   # change it to tuple because Dictionary keys must be immutable types. 
            if (pos[0], pos[1]) in graph.father:     # pos already in father, meaning it's been connected, append the cnt ot res
                res.append(graph.cnt)
                continue

            graph.add(pos)      # if pos not in father, then we should add it to father first, note that cnt++ at his time

            for move in self.MOVES:    
                new_pos = (pos[0] + move[0], pos[1] + move[1])

                # if new_idx in graph.father, meaning the new_idx place already has a 1, 
                # then we should connect idx and new_idx on the graph and cnt -= 1, because there is one less isolated islands after connection
                if 0 <= new_pos[0] < m and 0 <= new_pos[1] < n and new_pos in graph.father:
                    graph.connect(pos, new_pos)

            res.append(graph.cnt)
                            
        return res
