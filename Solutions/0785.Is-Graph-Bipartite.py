"""
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

        
"""
solution 2: dfs, mark the color of nodes as we go.  O(V+E)
"""
class Solution:
    def isBipartite(self, edges: List[List[int]]) -> bool:
        def dfs(curr_node, curr_color):
            visited[curr_node] = curr_color
            
            for next_node in edges[curr_node]:
                if next_node in visited:
                    if visited[next_node] == curr_color:
                        return False
                    continue
                if not dfs(next_node, not curr_color):  # 在这里调用dfs是模板的分内之事，这题return True/False, 所以在这里check
                    return False
                
            return True
        
        # have to do dfs for every node cuz it could be a biparitite even if there are lots of dis-connected components in the graph
        visited = defaultdict(bool)         # True表示red color, False表示blue color
        for node in range(len(edges)):      # for loop保证可以访问到所有的nodes
            if node not in visited:         # 注意这里要check in visited
                if not dfs(node, True):
                    return False
        return True



"""
solution 1: bfs, visit every node and label their color every other step. O(V+E)
"""
class Solution:
    def isBipartite(self, lists: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for i, lst in enumerate(lists):
            graph[i] = lst
            
        colormap = collections.defaultdict(str)   # key is the node, value is the color
        
        # have to do bfs for every node cuz it could be a biparitite even if there are lots of dis-connected components in the graph
        for node in range(len(graph)):  # have to visit every node exactly once O(V)
            if node not in colormap:    # colormap 相当于visited
                if not self._bfs(node, graph, colormap):
                    return False
        return True
         
    def _bfs(self, node, graph, colormap):
        q = collections.deque()
        q.append(node)
        colormap[node] = "red"
        red = True          # boolean should be labeled red?
        while len(q) > 0:
            red = not red
            lens = len(q)
            for _ in range(lens):   # 这里必须要层序遍历
                curr_node = q.popleft()
                for next_node in graph[curr_node]:  # have to visite evry edge exactly once O(E)
                    if next_node in colormap:
                        if colormap[next_node] == colormap[curr_node]:
                            return False    # 如果next_node已经在colormap里了，现在又必须要换一种颜色，那么说明next_node 涂成red也不行blue也不行, return False
                        continue
                    q.append(next_node)
                    colormap[next_node] = "red" if red else "blue"
        return True
        
