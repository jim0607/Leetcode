"""
1066. Campus Bikes II

On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

 
Example 1:


Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: 6
Explanation: 
We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.
Example 2:



Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: 4
Explanation: 
We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker 2, bike 2 to worker 2 or worker 1. Both assignments lead to sum of the Manhattan distances as 4.
"""


"""
backtrack结束条件：len(assigned_workers) == n
constraint on next_candidate: the worker is not in assigned_workers, the bike is not in assigned_bikes
arguments pass into backtrack function: curr_dist
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def backtrack(curr_dist):
            if len(assigned_workers) == len(workers):
                self.min_dist = min(self.min_dist, curr_dist)
                return
            
            for next_w in range(len(workers)):
                if next_w not in assigned_workers:
                    for next_b in range(len(bikes)):
                        if next_b not in assigned_bikes:
                            assigned_workers.add(next_w)
                            assigned_bikes.add(next_b)
                            backtrack(curr_dist + abs(workers[next_w][0] - bikes[next_b][0]) + abs(workers[next_w][1] - bikes[next_b][1]))
                            assigned_workers.remove(next_w)
                            assigned_bikes.remove(next_b)
            
                
        self.min_dist = sys.maxsize
        assigned_workers = set()
        assigned_bikes = set()
        backtrack(0)
        return self.min_dist

       


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:   
        def dist(w, b):
            return abs(w[0] - b[0]) + abs(w[1] - b[1])
        
        def dfs(curr_w, assigned_bikes, memo):
            """
            curr_w: curr idx for workers
            """
            if curr_w == len(workers):
                return 0
            
            if (curr_w, tuple(assigned_bikes)) in memo:     # change set to tuple cuz set is not hashable
                return memo[(curr_w, tuple(assigned_bikes))]
            
            res = float("inf")
            for next_b in range(len(bikes)):
                if next_b in assigned_bikes:
                    continue
                
                next_dist = dist(workers[curr_w], bikes[next_b])
                
                assigned_bikes.add(next_b)
                res = min(res, next_dist + dfs(curr_w + 1, assigned_bikes, memo))
                assigned_bikes.remove(next_b)       # backtrack, 指数级别的复杂度
                
            memo[(curr_w, tuple(assigned_bikes))] = res
            
            return res
        
        memo = collections.defaultdict()
        assigned_bikes = set()
        
        return dfs(0, assigned_bikes, memo)
       
       
       
       
       
"""
solution 2: backtrack + Dijkstra's
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def dist(w, b):
            return abs(w[0] - b[0]) + abs(w[1] - b[1])
        
        assigned_bikes = set()
        hq = [(0, 0, tuple(assigned_bikes))]  # (curr_cost, number_of_assigned_workers, assigned_bikes)
        optimal = collections.defaultdict(lambda: float("inf"))
        while len(hq) > 0:
            curr_cost, assigned_workers_cnt, assigned_bikes = heappop(hq)
            assigned_bikes = set(assigned_bikes)
            if assigned_workers_cnt == len(workers):
                return curr_cost            
            for bike_id, bike_pos in enumerate(bikes):
                if bike_id in assigned_bikes:
                    continue
                assigned_bikes.add(bike_id)
                next_cost = curr_cost + dist(workers[assigned_workers_cnt], bike_pos)
                if next_cost < optimal[(assigned_workers_cnt, tuple(assigned_bikes))]:
                    optimal[(assigned_workers_cnt, tuple(assigned_bikes))] = next_cost
                    heappush(hq, (next_cost, assigned_workers_cnt + 1, tuple(assigned_bikes)))
                assigned_bikes.remove(bike_id)
        return -1
