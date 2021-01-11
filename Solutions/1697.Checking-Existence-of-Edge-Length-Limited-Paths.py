"""
1697. Checking Existence of Edge Length Limited Paths

An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. 
Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] 
whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj.

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

Example 1:

Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.


"""
loope over the queries, each query is a dijkstra's to find min_max problem.
O(QVlogV), Q is how many queries are there, V is how many nodes are there.
"""
class Solution:
    def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dijkstra(start, end):   # O(VlogV)
            hq = [(0, start)]     # min heap for maxcost
            costs = defaultdict(int)    # curr_node --> min_maxcost to curr_node
            
            while len(hq) > 0:
                curr_min_maxcost, curr_node = heappop(hq)
                if curr_node == end:
                    return curr_min_maxcost
                
                if curr_node in costs:
                    continue
                costs[curr_node] = curr_min_maxcost
                
                for next_node, next_cost in graph[curr_node].items():
                    next_maxcost = max(next_cost, curr_min_maxcost)
                    heappush(hq, (next_maxcost, next_node))
                
            return sys.maxsize
        
        # step 1: build the graph, Note that there may be multiple edges between two nodes.
        graph = defaultdict(lambda: defaultdict(lambda: sys.maxsize))
        for u, v, cost in edges:
            graph[u][v] = min(graph[u][v], cost)
            graph[v][u] = min(graph[v][u], cost)
                
        res = []
        for u, v, limit in queries:
            min_maxcost = dijkstra(u, v)
            if min_maxcost < limit:
                res.append(True)
            else:
                res.append(False)
        return res
        
        
"""
solution 2: union find by rank. I think dikstra's is enough for this problem.
"""
