#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
# https://leetcode.com/problems/clone-graph/description/
#
# algorithms
# Medium (30.36%)
# Likes:    1194
# Dislikes: 1156
# Total Accepted:    273.1K
# Total Submissions: 894K
# Testcase Example:  '{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}'
#
# Given a reference of a node in a connected undirected graph, return a deep
# copy (clone) of the graph. Each node in the graph contains a val (int) and a
# list (List[Node]) of its neighbors.
# 
# 
# 
# Example:
# 
# 
# 
# 
# Input:
# 
# {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
# 
# Explanation:
# Node 1's value is 1, and it has two neighbors: Node 2 and 4.
# Node 2's value is 2, and it has two neighbors: Node 1 and 3.
# Node 3's value is 3, and it has two neighbors: Node 2 and 4.
# Node 4's value is 4, and it has two neighbors: Node 1 and 3.
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes will be between 1 and 100.
# The undirected graph is a simple graph, which means no repeated edges and no
# self-loops in the graph.
# Since the graph is undirected, if node p has node q as neighbor, then node q
# must have node p as neighbor too.
# You must return the copy of the given node as a reference to the cloned
# graph.
# 
#
"""deep copy意味着所有的节点都一样，但是与原图存放的地址不一样，所以原图发生任何改变都不会影响到copy的那个图
分三步：1. 找到所有的node
2. 复制所有的node
3. 找到和复制所有节点对应的边/邻居"""
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        root = node

        # 第一步：找到所有的点，用BFS实现
        nodes = self.getNodes(node)

        # 第二步：复制所有的node，存到mapping中，边可以先设为空
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val, [])       

        # 第三步：复制所有节点对应的边/邻居
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    # BFS get all the nodes
    def getNodes(self, node):
        q = collections.deque()
        q.append(node)
        res = set()
        res.add(node)
        while q:
            currNode = q.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in res:
                    res.add(neighbor)
                    q.append(neighbor)

        return res 

# @lc code=end

