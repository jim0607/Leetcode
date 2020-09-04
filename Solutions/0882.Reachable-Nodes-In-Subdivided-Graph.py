882. Reachable Nodes In Subdivided Graph

Starting with an undirected graph (the "original graph") with nodes from 0 to N-1, subdivisions are made to some of the edges.

The graph is given as follows: edges[k] is a list of integer pairs (i, j, n) such that (i, j) is an edge of the original graph,

and n is the total number of new nodes on that edge. 

Then, the edge (i, j) is deleted from the original graph, n new nodes (x_1, x_2, ..., x_n) are added to the original graph,

and n+1 new edges (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j) are added to the original graph.

Now, you start at node 0 from the original graph, and in each move, you travel along one edge. 

Return how many nodes you can reach in at most M moves.


Example 1:

Input: edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
Output: 13
Explanation: 
The nodes that are reachable in the final graph after M = 6 moves are indicated below.

Example 2:

Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
Output: 23
 

Note:

0 <= edges.length <= 10000
0 <= edges[i][0] < edges[i][1] < N
There does not exist any i != j for which edges[i][0] == edges[j][0] and edges[i][1] == edges[j][1].
The original graph has no parallel edges.
0 <= edges[i][2] <= 10000
0 <= M <= 10^9
1 <= N <= 3000
A reachable node is a node that can be travelled to using at most M moves starting from node 0.



"""
Time Complexity: Dijkstra + Heap is O(ElogE)
"""
class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, insert_cnt in edges:
            graph[u].append((v, insert_cnt))
            graph[v].append((u, insert_cnt))
            
        hq = [(-M, 0)]          # (currently how many moves left, curr_node)
        moves_left = collections.defaultdict(int)
        
        while len(hq) > 0:
            curr_moves_left, curr_node = heappop(hq)  # 贪心就贪在这，每次pop出来的都是剩余步数最多（即离soure node最近）的node
            curr_moves_left = -curr_moves_left
            
            if curr_node in moves_left:     # if we have already reached this node with less steps, then just skip it
                continue
            moves_left[curr_node] = curr_moves_left
            
            for next_node, insert_cnt in graph[curr_node]:
                if insert_cnt >= curr_moves_left:   # we cannot reach the nextNode if there is not enough moves left
                    continue
                heappush(hq, (-(curr_moves_left - insert_cnt - 1), next_node))
                
        res = len(moves_left)
        for u, v, insert_cnt in edges:
            res += min(moves_left[u] + moves_left[v], insert_cnt)
        return res
