"""
Amazon | OA 2019 | Min Cost to Repair Edges

There's an undirected connected graph with n nodes labeled 1..n. But some of the edges has been broken disconnecting the graph. 
Find the minimum cost to repair the edges so that all the nodes are once again accessible from each other.

Input:
n, an int representing the total number of nodes.
edges, a list of integer pair representing the nodes connected by an edge.
edgesToRepair, a list where each element is a triplet representing the pair of nodes between which an edge is currently broken and the cost of repearing that edge, respectively (e.g. [1, 2, 12] means to repear an edge between nodes 1 and 2, the cost would be 12).
Example 1:

Input: n = 5, edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], edgesToRepair = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
Output: 20
Explanation:
There are 3 connected components due to broken edges: [1], [2, 3] and [4, 5].
We can connect these components into a single component by repearing the edges between nodes 1 and 2, and nodes 1 and 5 at a minimum cost 12 + 8 = 20.
Example 2:

Input: n = 6, edges = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], edgesToRepair = [[1, 6, 410], [2, 4, 800]]
Output: 410
Example 3:

Input: n = 6, edges = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]], edgesToRepair = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
Output: 79
"""

"""
Solution:
Apply Kruskal's algorithm: Just take existing edges to have 0 cost and broken edges have their given cost.
And find minimum spanning tree cost will be the answer.
"""
class Solution:
    def minCostToRepairEdges(self, n: int, existing_edges: List[int], edgesToRepair: List[List[int]]) -> int:
        uf = UnionFind(n)
        
        edges = edgesToRepair           # Just take broken edges to have their given cost.
        for u, v in existing_edges:     # and the existing edges to have 0 cost
            edges.append([u, v, 0])
            
        edges.sort(key = lambda x: x[2])
        
        costs = 0
        for u, v, cost in edges:
            if uf.connected(u, v):
                continue
            uf.union(u, v)
            costs += cost
        
        return costs if uf.cnt = 1 else -1  # 如果self.cnt != 1的话那就说明这些水管修不好了
    
    
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

