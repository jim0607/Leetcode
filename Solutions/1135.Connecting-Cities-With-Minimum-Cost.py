1135. Connecting Cities With Minimum Cost

There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.

Example 1:

Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:

Input: N = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: 
There is no way to connect all cities even if all edges are used.


"""
"""
This problem is to find the minimum path to connect all nodes, so it is a minimum spanning tree (MST) problem.
There are two defferent algorithms to solve MST problem, one is Prim's, the other is Kruskal's.
The Kruskul's algorithm is easy to implement using Union-Find, with O(ElogE) time and O(V) space.
step 1: put all vertices into the uf graph;
step 2: sort the edges;
step 3: put each edge into the graph if not forming cycle;
(if the two vertices of the edge was already connected, then adding this edge will form a cycle);
step 4: keep doing step 3 until all vertices connected (self.disjoint_cnt = 1)
"""
"""

class UnionFind:
    def __init__(self, N):
        self.father = collections.defaultdict()
        self.disjoint_cnt = 0
        
        for i in range(1, N + 1):                                   # O(V) sapce for Union-Find
            self.father[i] = i
            self.disjoint_cnt += 1
        
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def connected(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return True
        return False
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.disjoint_cnt -= 1
            

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        uf = UnionFind(N)                                           # add all the vertices into the union-find obj
        connections.sort(key = lambda connection: connection[2])    # sort the graph as that we always add the smallest edge
        total_cost = 0
        for u, v, cost in connections:
            if uf.connected(u, v):                                  # continue so that there will be no cycle
                continue
            uf.union(u, v)
            total_cost += cost
            
        return total_cost if uf.disjoint_cnt == 1 else -1           # if uf.disjoint_cnt > 1, meaning we are not able to connect all cities.
                                                                    # That is to say, we have a MST forest instead of a single MST.
