"""
743. Network Delay Time

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, 
v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 1. construct a graph represented by a dictionary of adjaency list
        graph = collections.defaultdict(list)       # 根据边构建图 O(E)
        for u, v, time in times:
            graph[u].append((v, time))
            
        # 2. bfs using heapq
        hq = [(0, K)]                            # maintian a min heap to keep track of min time
        distance = collections.defaultdict(int)  # store the distance of each node to node K, 这个extra space必不可少是用来换时间的
        
        while len(hq) > 0:      # O(VlogV)
            curr_dist, curr_node = heappop(hq)
            
            if curr_node in distance:            # 可以continue的前提是我们每次pop出来的都是最lowest cost的路径，
                continue  # 如果已经用最优路径访问过currNode了，接下来再次访问该node肯定不会是最low cost的了，所以可以continue
            distance[curr_node] = curr_dist
            
            for next_node, next_dist in graph[curr_node]:   # Dijkstra算法里：next这一层只干一件事：那就是把这个nextNode push到hq中
                heappush(hq, (curr_dist + next_dist, next_node))    # 千万不要在这里更新distance, 
                                            # 因为不能保证哪个neighbor是low cost的选择，只有push进去之后再pop出来的才是最low cost的
        return max(dist for dist in distance.values()) if len(distance) == N else -1  # len(distance) == N 判断每个点都能访问到
