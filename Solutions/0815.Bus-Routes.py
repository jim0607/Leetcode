815. Bus Routes

We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.


"""
Shortest path problem: bfs. 与word ladder那题类似，word ladder是one-to-one的bfs, 这个是多源节点出发的bfs.
solution 1: q里面放route idx.
"""
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        
        # 首先建立一个stop_to_route的dictionary, 方便从当前stop找下一个stop
        stop_to_route = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_route[stop].add(i)
        
        q = collections.deque()
        visited = set()
        for idx in stop_to_route[S]:
            q.append(idx)
            visited.add(idx)
            
        steps = 0
        while q:
            lens = len(q)
            steps += 1
            for _ in range(lens):
                curr_idx = q.popleft()
                
                for stop in routes[curr_idx]:
                    if stop == T:
                        return steps
                    for next_idx in stop_to_route[stop]:
                        if next_idx not in visited:
                            q.append(next_idx)
                            visited.add(next_idx)
                            
        return -1

    
    
"""
solution 2: q里面放stop
"""
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], start: int, end: int) -> int:
        routes = [set(route) for route in routes]
        
        # constructe stop_to_route_idx for fast route loop up
        stop_to_route = collections.defaultdict(list)
        for idx, route in enumerate(routes):
            for stop in route:
                stop_to_route[stop].append(idx)
        
        q = collections.deque()
        visited = set()
        q.append(start)
        visited.add(start)
        
        stops = -1
        while len(q) > 0:
            stops += 1
            lens = len(q)
            for _ in range(lens):
                curr_stop = q.popleft()
                if curr_stop == end:
                    return stops
                for next_stop in self._get_next(routes, stop_to_route, visited, curr_stop):
                    q.append(next_stop)
                    visited.add(next_stop)
        return -1
                    
    def _get_next(self, routes, stop_to_route, visited, curr_stop):
        res = []
        for idx in stop_to_route[curr_stop]:    # get the route that inludes the stop
            for stop in routes[idx]:            # get the stop that is in the route
                if stop not in visited:
                    res.append(stop)
        return res
