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
"""判断图是不是一棵树（不一定非要是二叉树）需要满足两点：
1. 首先点的数目一定比边的数目多一个
2. 然后要确保no isolated node and no cycle，也即是保证每个点都能被访问且只被访问了一次，
也就是visited的数目要等于节点数目"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return Ture

        if len(edges) != n - 1:  # 首先点的数目一定比边的数目多一个
            return False

        # 图的实现方法是使用hashmap，key是int表示节点, value是set(int)表示该节点所连接的相邻节点。
        neighbors = collections.defaultdict(list)       # 这里必须声明是一个list, 否则后面append会报错
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        
        from collections import deque
        q = deque()
        visited = set()      # 与二叉树的BFS相比多加了一行visited
        q.append(0)
        visited.add(0)  # visited and q are twin brothers, whenever q append something, visited add something
        
        while q:
            currNode = q.popleft()
            for node in neighbors[currNode]:  # 这里体现BFS，首先访问currNode节点的所有邻居节点
                # 如果已经访问过就不再访问了，这样可以保证每个节点都被访问过一次
                if node not in visited:     # 没访问过就加入队列
                    q.append(node)
                    visited.add(node)       # twin brothers
        
        return len(visited) == n    # 每个节点都被访问过且都被访问过一次
    
    
    
class UnionFind:
    def __init__(self):
        self.father = collections.defaultdict()
        self.cnt = 0    # the total number of isolated components in the graph
        
    def add(self, x):
        """
        add node x in the graph
        """
        self.father[x] = x
        self.cnt += 1
        
    def find(self, x):
        """
        find the root of x in the graph using path compression
        """
        if self.father[x] == x:
            return x
        
        self.father[x] = self.find(self.father[x])
        
        return self.father[x]
    
    def connect(self, a, b):
        """
        connect node a and node b
        """
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt -= 1
    
"""
Solution 2: Dynamic connection problem: Union Find
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:     # 边数必须比点数少1
            return False
        if n == 1:
            return True
        
        graph = UnionFind()
        
        for edge in edges:
            if edge[0] not in graph.father and edge[1] not in graph.father:
                graph.add(edge[0])
                graph.add(edge[1])
                graph.connect(edge[0], edge[1])
            
            elif edge[0] in graph.father and edge[1] not in graph.father:
                graph.add(edge[1])
                graph.connect(edge[0], edge[1])
            
            elif edge[1] in graph.father and edge[0] not in graph.father:
                graph.add(edge[0])
                graph.connect(edge[0], edge[1])
                
            elif edge[0] in graph.father and edge[1] in graph.father:
                if graph.cnt == 1:      # 本来edge[0]和edge[1]都已经连好了，还要再连一下，那就不对了
                    return False
                graph.connect(edge[0], edge[1])
            
        return graph.cnt == 1
