1129. Shortest Path with Alternating Colors

Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

 

Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]
Example 3:

Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]
Example 4:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]
Example 5:

Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]


"""
这一题的题眼是visiting the same node with same color is not allowed, with same color is not.
所以color信息要放到adjacency list 里，也要放到q里，还要放到visited里
"""
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # step 1: change the array of edges representation to adjacency list
        graph = collections.defaultdict(list)    # list stores (neighbor, edge color)
        for u, v in red_edges:
            graph[u].append((v, "RED"))
        for u, v in blue_edges:
            graph[u].append((v, "BLUE"))
            
        # step 2: traversal the graph and update the res
        # we want to find the shorted steps, so use bfs
        res = [-1 for _ in range(n)]
        q = collections.deque()
        visited = set()
        q.append((0, "ORIGIN"))
        visited.add((0, "ORIGIN"))   # visiting the same node with same color is not allowed, with same color is not
        step = -1
        while q:
            step += 1
            lens = len(q)
            for _ in range(lens):
                curr_node, curr_color = q.popleft()
                if res[curr_node] == -1: res[curr_node] = step      # update res
                for next_node, next_color in graph[curr_node]:
                    if (next_node, next_color) in visited:  # visiting the same node with same color is not allowed
                        continue
                    if next_color == curr_color:    
                        continue
                    q.append((next_node, next_color))
                    visited.add((next_node, next_color))
        return res        
