591. Connecting Graph III

Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:

connect(a, b), an edge to connect node a and node b
query(), Returns the number of connected component in the graph
Have you met this question in a real interview?  
Example
Example 1:

Input:
ConnectingGraph3(5)
query()
connect(1, 2)
query()
connect(2, 4)
query()
connect(1, 4)
query()

Output:[5,4,3,3]

Example 2:

Input:
ConnectingGraph3(6)
query()
query()
query()
query()
query()


Output:
[6,6,6,6,6]



class ConnectingGraph3:
    def __init__(self, n):
        self.father = collections.defaultdict(int)
        self.cnt = 0
        for i in range(1, n+1):
            self._add(i)
            
    def _add(self, x):
        self.father[x] = x
        self.cnt += 1
        
    def _find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self._find(self.father[x])
        return self.father[x]
    
    def connect(self, a, b):
        root_a, root_b = self._find(a), self._find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt -= 1

    def query(self):
        return self.cnt
