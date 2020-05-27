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
想想如果是一个很大的图，那minimum height trees的root就应该是这个图的最中心，所以我们就去找图的最中心就可以了，
采用从外围(inDegree=1的node)往中间走的方法，解法类似topological sort, 走到最后留下的顶点就是最中心的顶点，也就是距离所有外围顶点最小的顶点。
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # step 1: find inDegree information and neighbors information and store them in dict
        inDegrees = collections.defaultdict(int)
        neighbors = collections.defaultdict(list)
        for edge in edges:
            inDegrees[edge[0]] += 1
            inDegrees[edge[1]] += 1
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
            
        # step 2: bfs level by level to find the center most level
        q = collections.deque()
        for node, inDegree in inDegrees.items():    # putting all the outmost nodes inot th q
            if inDegree == 1:
                q.append(node)
                
        res = []    # res store the center most nodes
        while q:
            lens = len(q)
            level = []
            for _ in range(lens):
                currNode = q.popleft()
                level.append(currNode)
                for neighbor in neighbors[currNode]:
                    if inDegrees[neighbor] <= inDegrees[currNode]:      # 保证只从外围往中心走，类似word ladder II
                        continue
                    inDegrees[neighbor] -= 1
                    if inDegrees[neighbor] == 1:
                            q.append(neighbor)
                            
            res = level
            
        return res
