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


"""
用一个mapping 保存node-->node_copy. 然后一边dfs一边新建copied nodes
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        def dfs(node):
            for neighbor in node.neighbors:
                if neighbor in mapping:         # 注意这里不要continue
                    mapping[node].neighbors.append(mapping[neighbor])
                else:
                    mapping[neighbor] = Node(neighbor.val, [])
                    mapping[node].neighbors.append(mapping[neighbor])
                    dfs(neighbor)

        mapping = collections.defaultdict(Node)
        mapping[node] = Node(node.val, [])
        dfs(node)
        return mapping[node]



"""deep copy意味着所有的节点都一样，但是与原图存放的地址不一样，所以原图发生任何改变都不会影响到copy的那个图
分三步：Step 1：找到所有的original_nodes，存到一个set里面，用BFS实现
Step 2: 复制所有原有的node，存到mapping中，这样就建立了一个new_node和original_node的一一映射
Step 3: 复制所有original_node对应的neighbors 到 new_node里面"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        root = node
        
        # Step 1：找到所有的original_nodes，存到一个set里面，用BFS实现
        original_nodes = self.getAllNodes(node)
        
        # Step 2: 复制所有原有的node，存到mapping中，这样就建立了一个new_node和original_node的一一映射
        mapping = collections.defaultdict(Node)
        for original_node in original_nodes:
            mapping[original_node] = Node(original_node.val, [])    # 先copy original_node.val
            
        # Step 3: 复制所有original_node对应的neighbors 到 new_node里面
        for original_node in original_nodes:
            new_node = mapping[original_node]
            for original_neighbor in original_node.neighbors:   # 再copy original_node.neighbors
                new_neighbor = mapping[original_neighbor]       # 注意这一句很容易漏掉，漏掉就不是clone了
                new_node.neighbors.append(new_neighbor)
            
        return mapping[root]
    
    def getAllNodes(self, node):
        dq = collections.deque()
        dq.append(node)
        nodesSet = set()
        nodesSet.add(node)
        
        while dq:
            currNode = dq.popleft()
            
            for neighbor in currNode.neighbors:
                if neighbor not in nodesSet:
                    dq.append(neighbor)
                    nodesSet.add(neighbor)
                    
        return nodesSet
