785. Is Graph Bipartite?

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.


"""
solution 1: bfs, visit every node and label their color every other step. O(V+E)
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colorDict = collections.defaultdict(int)   # key is the node, value is the color, -1 is red, 1 is blue
        
        # have to do bfs for every node cuz it could be a biparitite even if there are lots of dis-connected components in the graph
        for i in range(len(graph)):     # have to visit every node exactly once O(V)
            if i not in colorDict:
                if not self.bfs(graph, i, colorDict):
                    return False
        
        return True
            
    def bfs(self, graph, i, colorDict):
        q = collections.deque()
        q.append(i)
        red = True      # boolean should be labeled red?
        while q:
            red = not red
            lens = len(q)
            for _ in range(lens):
                currNode = q.popleft()
                colorDict[currNode] = -1 if red else 1
                for nextNode in graph[currNode]:    # have to visite evry edge exactly once O(E)
                    if nextNode in colorDict:
                        if colorDict[nextNode] == colorDict[currNode]:
                            return False
                        continue
                    q.append(nextNode)
                    
        return True       
        
        
"""
solution 2: dfs, mark the color of nodes as we go.  O(V+E)
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colorDict = collections.defaultdict(int)   # key is the node, value is the color, -1 is red, 1 is blue
        
        # have to do dfs for every node cuz it could be a biparitite even if there are lots of dis-connected components in the graph
        for i in range(len(graph)):     # have to visit every node exactly once O(V)
            if i not in colorDict:
                red = False
                if not self.dfs(graph, i, colorDict, red):
                    return False
        
        return True
        
    def dfs(self, graph, currNode, colorDict, red):
        """
        dfs the graph starting from i, mark the color on the way
        return whether or not there is a color violation on the way
        """
        red = not red
        colorDict[currNode] = -1 if red else 1
        for nextNode in graph[currNode]:
            if nextNode in colorDict:
                if colorDict[nextNode] == colorDict[currNode]:
                    return False
                continue
            if not self.dfs(graph, nextNode, colorDict, red):   # 在这里调用dfs是模板的分内之事，这题return True/False, 所以在这里check
                return False
            
        return True
