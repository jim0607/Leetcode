"""
1377. Frog Position After T Seconds

Given an undirected tree consisting of n vertices numbered from 1 to n. 
A frog starts jumping from the vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. 
The frog can not jump back to a visited vertex. In case the frog can jump to several vertices it jumps randomly to one of them with the same probability, 
otherwise, when the frog can not jump to any unvisited vertex it jumps forever on the same vertex. 

The edges of the undirected tree are given in the array edges, 
where edges[i] = [fromi, toi] means that exists an edge connecting directly the vertices fromi and toi.

Return the probability that after t seconds the frog is on the vertex target.

Example 1:

Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output: 0.16666666666666666 
Explanation: The figure above shows the given graph. The frog starts at vertex 1, 
jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability to vertex 4 after second 2. 
Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 
Example 2:

Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
Output: 0.3333333333333333
Explanation: The figure above shows the given graph. The frog starts at vertex 1, 
jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. 
Example 3:

Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6
Output: 0.16666666666666666
 
Constraints:

1 <= n <= 100
edges.length == n-1
edges[i].length == 2
1 <= edges[i][0], edges[i][1] <= n
1 <= t <= 50
1 <= target <= n
Answers within 10^-5 of the actual value will be accepted as correct.
"""



"""
虚拟一个节点零出来，从0节点出发做dfs. dfs the graph and update the dist of target and the prob of reaching target
"""
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)      # 注意是undirected tree，双向tree
        graph[0].append(1)          # 虚拟一个节点零出来，从0节点出发做dfs
        graph[1].append(0)
        
        self.prob = 1        # the prob to get to target node from node 1
        self.dist = -1       # the dist of target to node 1
        self.dfs(graph, 0, 1, -1, target, {0})    
        
        if self.dist > t:
            return 0
        if self.dist == t:
            return self.prob
        if self.dist < t:
            return self.prob if len(graph[target]) == 1 else 0   # target is a leaf if len(graph[target]) == 1

    
    def dfs(self, graph, curr_node, curr_prob, curr_dist, target, visited):
        """
        dfs the graph and update the dist of target and the prob of reaching target
        """
        if curr_node == target:
            self.prob = curr_prob
            self.dist = curr_dist
            return
        
        for next_node in graph[curr_node]:
            if next_node not in visited:
                visited.add(next_node)
                if len(graph[curr_node]) == 1:
                    self.dfs(graph, next_node, curr_prob, curr_dist + 1, target, visited)
                else:
                    self.dfs(graph, next_node, curr_prob / (len(graph[curr_node]) - 1), curr_dist + 1, target, visited)
