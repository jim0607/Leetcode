399. Evaluate Division

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


"""
Solution 1: bfs
注意这里构建图的时候是graph = collections.defaultdict(dict)  
in graph, key is node1, val is a dict of (key: node2, val: node1/node2)
Given the number of variables N, and number of equations E,
building the graph takes O(E), each query takes O(N), space for graph takes O(E)
I think if we start to compress paths, the graph will grow to O(N^2) gradually, and we can optimize each query to O(1), 
that is why we use global variable for graph, so that we can compress paths and avoid duplicated computing
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = collections.defaultdict(dict)  # key is node1, val is a dict of (key: node2, val: node1/node2)
        for [x, y], val in zip(equations, values):
            self.graph[x][y] = val
            self.graph[y][x] = 1 / val

        return [self.findDivision(query) for query in queries]
            
    def findDivision(self, query):
        startNode, endNode = query[0], query[1]
        if startNode not in self.graph or endNode not in self.graph:
            return -1
        if startNode == endNode:
            return 1.0
            
        q = collections.deque()
        visited = set()
        q.append((startNode, 1.0))
        visited.add(startNode)
            
        while q:
            currNode, currVal = q.popleft()
            for nextNode, nextVal in self.graph[currNode].items():
                if nextNode in visited:
                    continue       

                self.graph[startNode][nextNode] = nextVal * currVal  # update graph (path compression)
                self.graph[nextNode][startNode] = 1 / (nextVal * currVal)
                
                q.append((nextNode, nextVal * currVal))
                visited.add(nextNode)
                
               #  print((nextNode, endNode))
                if nextNode == endNode:
                    return self.graph[startNode][nextNode]
                
        return -1.0



"""
solution 2: Union Find
since we need to use paths compression to enable efficient query, we can use union find.
"""



"""
solution 3: 弗洛伊德算法
"""
def calcEquation(self, edges, weights, pairs):
     
    graph = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))
     
    for (i, j), weight in itertools.izip(edges, weights):
        graph[i][i], graph[i][j], graph[j][i], graph[j][j] = 1., weight, 1. / weight, 1.
     
    for mid in graph:
        for i in graph[mid]:
            for j in graph[mid]:
                graph[i][j] = min(graph[i][j], graph[i][mid] * graph[mid][j])
     
    return [graph[i][j] if graph[i][j] < float('inf') else -1. for i, j in pairs]
