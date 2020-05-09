591. Connecting Graph II

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
        self.father = collections.defaultdict()
        self.cnt = n
        
        for i in range(1, n + 1):
            self.father[i] = i
        
    def find(self, x):
        if self.father[x] == x:
            return x
            
        self.father[x] = self.find(self.father[x])
        
        return self.father[x]
    
    def connect(self, a, b):
        father_a, father_b = self.find(a), self.find(b)
        
        if father_a != father_b:
            self.father[father_b] = father_a
            self.cnt -= 1

    def query(self):
        return self.cnt
