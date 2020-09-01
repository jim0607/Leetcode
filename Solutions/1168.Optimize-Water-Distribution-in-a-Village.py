1168. Optimize Water Distribution in a Village

There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i], or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes, where each pipes[i] = [house1, house2, cost] represents the cost to connect house1 and house2 together using a pipe. Connections are bidirectional.

Find the minimum total cost to supply water to all houses.

 

Example 1:

Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: 
The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.



"""
Kruskal's 模板
"""
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        uf = UnionFind(n + 1)
        
        edges = pipes                       # 这个题目比较tricky的地方是需要想像有一个虚拟的house_0, house_0是出水的house 
        for i, cost in enumerate(wells):    # 这样house_1自己打井需要的cost就相当于从house_0连接到house_1所需的cost了
            edges.append([0, i+1, cost])
            
        edges.sort(key = lambda x: x[2])
        
        costs = 0
        for u, v, cost in edges:
            if uf.connected(u, v):
                continue
            uf.union(u, v)
            costs += cost
        
        return costs
    
    
class UnionFind:
    
    def __init__(self, N):
        self.father = collections.defaultdict(int)
        self.cnt = 0
        for i in range(N):
            self.add(i)
            
    def add(self, x):
        self.father[x] = x
        self.cnt += 1
        
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def connected(self, a, b):
        return self.find(a) == self.find(b)
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt -= 1
