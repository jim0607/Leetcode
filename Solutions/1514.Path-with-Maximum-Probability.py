"""
1514. Path with Maximum Probability

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
"""

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)  # node --> (neib_node, cost)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
            
        hq = [(-1, start)]
        costs = defaultdict(int)    # curr_node --> max_prob to curr_node
        while len(hq) > 0:
            curr_cost, curr_node = heappop(hq)
            curr_cost = -curr_cost
            
            if curr_node == end:
                return curr_cost
            
            if curr_node in costs:
                continue
            costs[curr_node] = curr_cost
            
            for next_node, next_cost in graph[curr_node]:
                heappush(hq, (-curr_cost * next_cost, next_node))
                
        return 0.0





import math

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, math.log10(succProb[i])))   # 用log是为了避免小数相乘最后变成0.000000
            graph[v].append((u, math.log10(succProb[i])))
        
        hq = [(0, start)]
        probability = collections.defaultdict(float)      # 所有的Dijkstra这个dictionary都是需要的
        while len(hq) > 0:
            curr_prob, curr_node = heappop(hq)
            curr_prob = -curr_prob
            if curr_node == end:
                return 10**curr_prob
                
            if curr_node in probability:
                continue
            probability[curr_node] = curr_prob
            
            for next_node, next_prob in graph[curr_node]:
                if next_node not in probability:        # 这一句可以要也可以不要
                    heappush(hq, (-(curr_prob + next_prob), next_node))   # 维护一个最大堆
            
        return 0
