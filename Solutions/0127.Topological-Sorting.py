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



""""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # 1. collect indgree information of each node an store in a dict
        in_degrees = collections.defaultdict(int)
        for node in graph:
            if node not in in_degrees:
                in_degrees[node] = 0
            for n in node.neighbors:
                in_degrees[n] += 1
        
        # 2. topological sorting - bfs
        q = collections.deque()
        for node in graph:
            if in_degrees[node] == 0:   # 初始化q，一般是q.append(根)，这里是把indegree==0的node 入队列
                q.append(node)
                
        res = []
        while len(q) > 0:
            curr_node = q.popleft()
            res.append(curr_node)    # 孪生兄弟
            for next_node in curr_node.neighbors:
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 0:  # 这个判断相当于模板里visited的判断，因为没有一个节点的indgree能两次成为0，所以这个判断可以保证每个节点被访问一次
                    q.append(next_node)     # always append the in_degree = 0 nodes into queue
        return res
    
    
        """
        follow up question: what if topological order 在这个图中不存在，怎么办？也就是说如果出现了环状依赖的节点怎么办？
        if len(res) == len(graph):
            return res
        else:
            return None
        """
