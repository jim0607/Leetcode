834. Sum of Distances in Tree

An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.

The ith edge connects nodes edges[i][0] and edges[i][1] together.

Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.

Example 1:

Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: 
Here is a diagram of the given tree:
  0
 / \
1   2
   /|\
  3 4 5
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.



"""
Good explanation here: https://leetcode.com/problems/sum-of-distances-in-tree/discuss/130567/Two-traversals-O(N)-python-solution-with-Explanation
  0
 / \
1   2
   /|\
  3 4 5
"""
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        cnt = [1 for _ in range(N)]         # cnt[i] = how many nodes does node i has in its subtree
        sum_dist = [0 for _ in range(N)]    # sum_dist[i] = the sum of dist from node i to all nodes
        
        def dfs(curr_node, prev_node):
            for next_node in graph[curr_node]:
                if next_node == prev_node:
                    continue
                dfs(next_node, curr_node)
                cnt[curr_node] += cnt[next_node]
                sum_dist[curr_node] += sum_dist[next_node] + cnt[next_node]


                
        def dfs2(curr_node, prev_node):
            for next_node in graph[curr_node]:
                if next_node == prev_node:
                    continue
                sum_dist[next_node] = sum_dist[curr_node] + N - 2 * cnt[next_node]
                dfs2(next_node, curr_node)
                
        dfs(0, -1)
        dfs2(0, -1)
        
        return sum_dist
