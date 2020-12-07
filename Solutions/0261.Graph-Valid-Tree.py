#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#
# https://leetcode.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (40.90%)
# Likes:    811
# Dislikes: 27
# Total Accepted:    108.4K
# Total Submissions: 264.7K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge
# is a pair of nodes), write a function to check whether these edges make up a
# valid tree.
# 
# Example 1:
# 
# 
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# 
# Example 2:
# 
# 
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
# 
# Note: you can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0,1] is the same as [1,0] and thus will not appear
# together in edges.
# 
#




"""
Solution 1: union find: 两个判断标准: 1. 无环, if uf.connected(i, j): return False. 
2. 整张图只有一个disjoint_cnt, return self.disjoint_cnt == 1.
"""
class UnionFind:
    
    def __init__(self, n):
        self.father = collections.defaultdict(int)
        self.cnt = 0
        
        for i in range(n):      # 把n个节点都放进图中 O(V)
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


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        
        for i, j in edges:          # O(E)
            if uf.connected(i, j):  # 如果i和j节点已经connected, 现在还要连接他们就会形成环
                return False
            
            uf.union(i, j)
            
        return uf.cnt == 1


    
"""
dfs 写法更简洁
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:  # 首先点的数目一定比边的数目多一个
            return False

        graph = collections.defaultdict(list) 
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set() 
        self._dfs(graph, 0, visited)
        
        return len(visited) == n    # 每个节点都被访问过且都被访问过一次
        
    def _dfs(self, graph, curr_node, visited):
        visited.add(curr_node)
        
        for next_node in graph[curr_node]:
            if next_node not in visited:
                self._dfs(graph, next_node, visited)

    


"""
判断图是不是一棵树（不一定非要是二叉树）需要满足两点：
1. 首先点的数目一定比边的数目多一个
2. 然后要确保no isolated node and no cycle，也即是保证每个点都能被访问且只被访问了一次，
也就是visited的数目要等于节点数目
"""
cclass Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return Ture

        if len(edges) != n - 1:  # 首先点的数目一定比边的数目多一个
            return False

        # 图的实现方法是使用a dictionary of adjacency nodes，key是int表示节点, value是set(int)表示该节点所连接的相邻节点。
        graph = collections.defaultdict(list)       # 这里必须声明是一个list, 否则后面append会报错
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()     # 与二叉树的BFS相比多加了一行visited
        self._bfs(graph, visited)
        
        return len(visited) == n    # 每个节点都被访问过且都被访问过一次
        
    def _bfs(self, graph, visited):
        q = collections.deque()
        q.append(0)
        visited.add(0)  # visited and q are twin brothers, whenever q append something, visited add something
        
        while len(q) > 0:
            currNode = q.popleft()
            for node in graph[currNode]:  # 这里体现BFS，首先访问currNode节点的所有邻居节点
                if node not in visited:   # 如果已经访问过就不再访问了，这样可以保证每个节点都被访问过一次, 没访问过就加入队列
                    q.append(node)
                    visited.add(node)     # twin brothers
