127. Topological Sorting
中文English
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

Example
For graph as follow:

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
Challenge
Can you do it in both BFS and DFS?

Clarification
Learn more about representation of graphs

Notice
You can assume that there is at least one topological order in the graph.


"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

"""分两步：1. collect indgree of each node
2. topological sorting - bfs"""

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return
        
        # 1. collect indgree of each node
        indgree = self.getIndgree(graph)
        
        # 2. topological sorting - bfs
        order = []
        q = collections.deque()
        # 初始化q，一般是q.append(根)，这里是把indegree==0的node 入队列
        for n in graph:
            if indgree[n] == 0:
                q.append(n)
        
        # 接下来又进入模板时间
        while q:
            currNode = q.popleft()
            order.append(currNode)
            # bfs
            for neighbor in currNode.neighbors:
                indgree[neighbor] -= 1
                if indgree[neighbor] == 0:   # 这个判断相当于模板里visited的判断，因为没有一个节点的indgree能两次成为0，所以这个判断可以保证每个节点被访问一次。
                    q.append(neighbor)
        
        return order
        
    # 写完主程序之后再来写子程序
    def getIndgree(self, graph):
        indegree = collections.defaultdict()
        # 初始化indgree
        for n in graph:
            indegree[n] = 0
            
        for n in graph:
            for neighbor in n.neighbors:
                indegree[neighbor] += 1
        
        return indegree
        
                
                
