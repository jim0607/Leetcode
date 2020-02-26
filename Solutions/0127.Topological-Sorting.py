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


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return
        
        # 1. collect indgree information of each node an store in a dict
        inDegrees = collections.defaultdict(int)
        inDegrees = self.getInDegrees(graph)
        
        # 2. topological sorting - bfs
        res = []
        q = collections.deque()
        # 初始化q，一般是q.append(根)，这里是把indegree==0的node 入队列
        for node, inDegree in inDegrees.items():
            if inDegree == 0:
                q.append(node)
                res.append(node)        # 孪生兄弟
        
        # 模板时间
        while q:
            currNode = q.popleft()
            # 一层一层来
            for neighbor in currNode.neighbors:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:   # 这个判断相当于模板里visited的判断，因为没有一个节点的indgree能两次成为0，所以这个判断可以保证每个节点被访问一次。
                    q.append(neighbor)
                    res.append(neighbor)        # 孪生兄弟
        
        return res
    
        """follow up question: what if topological order 在这个图中不存在，怎么办？也就是说如果出现了环状依赖的节点怎么办？
        if len(order) == len(graph):
            return order
        else:
            return None
        """
        
    # 写完主程序之后再来写子程序
    def getInDegrees(self, graph):
        inDegrees = collections.defaultdict(int)
        # 初始化indgree
        for n in graph:
            inDegrees[n] = 0
            
        for node in graph:
            for neighbor in node.neighbors:
                inDegrees[neighbor] += 1
        
        return inDegrees
