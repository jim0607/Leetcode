310. Minimum Height Trees

For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]



"""
n = 4, edges = [[1,0],[1,2],[1,3]]
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # key is a node1, val is a dictionary connected to node1 (key: node2, val: distance to node1)
        self.graph = collections.defaultdict(lambda: collections.defaultdict(int))
        for node1, node2 in edges:
            self.graph[node1][node2] = 1
            self.graph[node2][node1] = 1
            
        allVisted = True
        for node in self.graph:
            allVisited = self.bfs(node)      # do a bfs to update the graph, so that we can know the distance of all nodes
            if not allVisited:
                return []
            
        print(self.graph)
        res = []
        minDist = float("inf")
        for node, neighbors in self.graph.items():
            maxDist = max(dist for dist in neighbors.values())
            if maxDist < minDist:
                minDist = maxDist
                while res:
                    res.pop()
                res.append(node)
            elif maxDist == minDist:
                res.append(node)
                
        return res
        
    def bfs(self, startNode):
        q = collections.deque()
        visited = set()
        q.append((startNode, 0))
        visited.add(startNode)
        
        while q:
            currNode, currDist = q.popleft()
            for nextNode, nextDist in self.graph[currNode].items():
                if nextNode in visited:
                    continue
                newDist = currDist + nextDist
                q.append((nextNode, newDist))
                visited.add(nextNode)
                
                self.graph[startNode][nextNode] = newDist   # update graph, 这里有重复计算距离，所以不对

        if len(visited) != len(self.graph):
            return False
        
        return True
