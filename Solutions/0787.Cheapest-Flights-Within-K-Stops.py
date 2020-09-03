787. Cheapest Flights Within K Stops

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.


"""
有向图，带权值，找从单源出发最佳路径问题：Dijkstra's algorithm O(NlogN + E)
与743相比少了一个currNode in costs: continue因为次好路径也可能是最后的结果，这是由于最好路径可能不满足stops<K
所以需要加一个 if currStops >= K: continue
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for flight in flights:      # O(E)
            graph[flight[0]].append((flight[1], flight[2]))
            
        hq = [(0, -1, src)]     # store (cost, stops, airports)
        costs = collections.defaultdict(int)    # key is airpot, val is the cost to reach that airport
        while hq:       # O(NlogN)
            currCost, currStops, currNode = heappop(hq)
            # if currNode in costs:   # 这一句不能要，因为如果最便宜的路径不满足 <= K stops的话，
            #     continue        # 我们还要回来找次便宜的路径，次便宜的路径可能也需要用到这个node, 所以不能continue掉
            # costs[currNode] = currCost
            
            if currNode == dst:
                return currCost
            
            if currStops >= K:  # 如果currStops已经等于K个了，那就不要再去找currNode的neighbhor了
                continue
                
            for nextNode, nextCost in graph[currNode]:      # Dijkstra算法里：neighbor这一层只干一件事：那就是把这个nextNode push到hq中
                heappush(hq, (currCost + nextCost, currStops + 1, nextNode))
                
        return -1

    
    
    
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # 1. construct the graph
        graph = collections.defaultdict(list)
        for u, v, cost in flights:
            graph[u].append((v, cost))
            
        # 2. bfs using hq
        hq = [(0, -1, src)]     # (curr_cost, curr_stops, curr_city)
        while len(hq) > 0:
            curr_cost, curr_stops, curr_city = heappop(hq)
            
            if curr_city == dst:
                return curr_cost
            
            if curr_stops >= K:
                continue
                
            for next_city, next_cost in graph[curr_city]:
                heappush(hq, (curr_cost + next_cost, curr_stops + 1, next_city))
                
        return -1
