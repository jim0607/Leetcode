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
class UnionFind:
    def __init__(self, N):
        self.father = collections.defaultdict()
        self.disjoint_cnt = 0
        
        for i in range(N + 1):     # O(V) sapce for Union-Find
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
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        uf = UnionFind(n)
        
        # 这个题目比较tricky的地方是需要想像有一个虚拟的house_0, house_0是出水的house 
        # 这样house_1自己打井需要的cost就相当于从house_0连接到house_1所需的cost了
        imaginary_pipes = []
        for i, well in enumerate(wells):
            imaginary_pipes.append([0, i + 1, well])
            
        pipes += imaginary_pipes    
        pipes.sort(key = lambda pipe: pipe[2])
        
        total_cost = 0
        for house_1, house_2, cost in pipes:
            if uf.connected(house_1, house_2):
                continue
            uf.union(house_1, house_2)
            total_cost += cost
        
        return total_cost if uf.disjoint_cnt == 1 else -1
