"""
1548. The Most Similar Path in a Graph

We have n cities and m bi-directional roads where roads[i] = [ai, bi] connects city ai with city bi. 
Each city has a name consisting of exactly 3 upper-case English letters given in the string array names. 
Starting at any city x, you can reach any city y where y != x (i.e. the cities and the roads are forming an undirected connected graph).

You will be given a string array targetPath. You should find a path in the graph of the same length and with the minimum edit distance to targetPath.

You need to return the order of the nodes in the path with the minimum edit distance, 
The path should be of the same length of targetPath and should be valid (i.e. there should be a direct road between ans[i] and ans[i + 1]). 
If there are multiple answers return any one of them.

The edit distance is defined as follows:

Example 1:

Input: n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = ["ATL","PEK","LAX","DXB","HND"], targetPath = ["ATL","DXB","HND","LAX"]
Output: [0,2,4,2]
Explanation: [0,2,4,2], [0,3,0,2] and [0,3,1,2] are accepted answers.
[0,2,4,2] is equivalent to ["ATL","LAX","HND","LAX"] which has edit distance = 1 with targetPath.
[0,3,0,2] is equivalent to ["ATL","DXB","ATL","LAX"] which has edit distance = 1 with targetPath.
[0,3,1,2] is equivalent to ["ATL","DXB","PEK","LAX"] which has edit distance = 1 with targetPath.
Example 2:

Input: n = 4, roads = [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], names = ["ATL","PEK","LAX","DXB"], targetPath = ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]
Output: [0,1,0,1,0,1,0,1]
Explanation: Any path in this graph has edit distance = 8 with targetPath.
Example 3:

Input: n = 6, roads = [[0,1],[1,2],[2,3],[3,4],[4,5]], names = ["ATL","PEK","LAX","ATL","DXB","HND"], targetPath = ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
Output: [3,4,5,4,3,2,1]
Explanation: [3,4,5,4,3,2,1] is the only path with edit distance = 0 with targetPath.
It's equivalent to ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
"""



"""
similar with 100320-Diff Between Two Strings - __DP to find path__
Step 1: build a DP table in order to find the minimum edit distance to targetPath;
Step 2: we traverse __reversely the build DP table__ to find which path did we take 
in order to get the minimum edit distance. At last, we return res[::-1].

dp[i][u] = the min edit distance if we take i steps, with u as the last city visited;
dp[i][u] = min(dp[i-1][v] for v in graph[u]) + 0 if names[u] == targetPath[i] else 1;
then min(dp[m]) is our minimum edit distance overall.
O(MN^2)
"""
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
            
        # step 1: build the DP table to find the minimum edit distance to targetPath
        m = len(targetPath)
        dp = [[sys.maxsize] * n for _ in range(m)]     
        for u in range(n):
            dp[0][u] = 0 if names[u] == targetPath[0] else 1
            
        for i in range(1, m):
            for u in range(n):
                for v in graph[u]:
                    dp[i][u] = min(dp[i][u], dp[i-1][v]) + 0
                dp[i][u] += 0 if names[u] == targetPath[i] else 1
                
                
        # step 2: 反向遍历the dp table to find the best path that leads to min_edit_dist
        # first we find the last min_dist_node, use it as the last node we take in the best path
        min_dist = sys.maxsize
        min_dist_node = -1
        for u in range(n):
            if dp[m-1][u] < min_dist:
                min_dist = dp[m-1][u]
                min_dist_node = u

        # then we reversely find each node in the best path
        res = [min_dist_node]
        curr_min = min_dist
        curr_min_node = min_dist_node
        for i in range(m - 2, -1, -1):   
            for v in graph[curr_min_node]:
                edit_dist = 0 if names[curr_min_node] == targetPath[i+1] else 1
                if dp[i][v] + edit_dist == curr_min:
                    curr_min = dp[i][v]
                    curr_min_node = v
                    res.append(v)
                    break       # 可能有多个u都等于curr_min, 我们只需要任意一个就可以
        return res[::-1]
        
        
"""
Follow-up: If each node can be visited only once in the path, What should you change in your solution?
has to use a list of visited set [set() * n for _ in range(m)] to armk those visited nodes in each path.
"""
