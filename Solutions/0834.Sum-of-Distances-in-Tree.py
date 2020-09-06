"""
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










"""
            X   -----------  y
          / | \            / | \
         o  o  o          o  o  o
        /|\                 /|\ 
       o o o               o o o 
       
sums[X] = sum of distances from X to other nodes
cnt[X] = total number of nodes in the subtree of X (including X)

sums(X) = X@X + Y@Y + cnt(Y), where X@X means sum of distances from X to subtree-nodes of X
sums(Y) = Y@Y + X@X + cnt(X)
sums(Y) - sums(X) = cnt(X) - cnt(Y)
sums(Y) = sums(X) + cnt(X) - cnt(Y) = sums(X) + (N - cnt(Y) - cnt(Y) = sums(X) + N - 2*cnt(X).

cnt[X]可以通过dfs遍历一次算出来存到一个list里面，这样我们如果已知sums(0)的话，
那么其余的sums(X)都可以通过上述公式算出来了
https://www.youtube.com/watch?v=gi2maECPOB0
"""
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        def dfs(curr_node, prev_node):
            for next_node in graph[curr_node]:
                if next_node == prev_node:
                    continue
                dfs(next_node, curr_node)
                cnt[curr_node] += cnt[next_node]    # 因为cnt[curr_node]需要next_node的信息，所以cnt在dfs之后更新
                sums[curr_node] += sums[next_node] + cnt[next_node]
                
        def dfs2(curr_node, prev_node):
            for next_node in graph[curr_node]:
                if next_node == prev_node:
                    continue
                sums[next_node] = sums[curr_node] + N - 2 * cnt[next_node]  # 因为sums[next_node]需要curr_node的信息，所以在dfs2之前更新
                dfs2(next_node, curr_node)      
        
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        sums = [0 for _ in range(N)]
        cnt = [1 for _ in range(N)]
        
        dfs(0, -1)  # 第一个dfs遍历tree得到cnt list, 并且得到sums for root node
        dfs2(0, -1)
        
        return sums
