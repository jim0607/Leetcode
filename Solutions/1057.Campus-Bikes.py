1057. Campus Bikes

On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with 
the shortest Manhattan distance between each other, and assign the bike to that worker. 
(If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; 
 if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.

 

Example 1:



Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: [1,0]
Explanation: 
Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].
Example 2:



Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: [0,2,1]
Explanation: 
Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is assigned to Bike 2, and Worker 2 will take Bike 1. 
So the output is [0,2,1].
 

Note:

0 <= workers[i][j], bikes[i][j] < 1000
All worker and bike locations are distinct.
1 <= workers.length <= bikes.length <= 1000



"""
brutal force solution: find the distance of all combinations, and sort them.
O(MNlog(MN))
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        all_combinations = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                all_combinations.append((dist, i, j))
                
        all_combinations.sort(key = lambda t: (t[0], t[1]))
        
        res = [-1] * len(workers)
        assigned_bikes = set()
        for dist, i, j in all_combinations:  # everytime, we deal with the smallest dist
            if res[i] == -1 and j not in assigned_bikes:
                res[i] = j
                assigned_bikes.add(j)
                
        return res
        
        
"""
bucket sort solution O(MN): find the distance of all combinations, and put them into bucket based on their distance. 
In this way, the distances are represented by idx, which were sort by nature.
Since the range of distance is [0, 2000] which is much lower than the # of pairs, which is 1e6. 
It's a good time to use bucket sort. Basically, it's to put each pair into the bucket representing its distance.
Eventually, we can loop thru each bucket from lower distance.
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # in the bucket, idx represents dist, val in the idx is a list of (workers, bikes) combinations
        buckets = [[] for _ in range(2001)]   # the bucket size is the range of distance
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                buckets[dist].append((i, j))
        
        res = [-1] * len(workers)
        assigned_bikes = set()
        for dist in buckets:  # everytime, we deal with the smallest dist, by looping thru idx/dist
            for i, j in dist:
                if res[i] == -1 and j not in assigned_bikes:
                    res[i] = j
                    assigned_bikes.add(j)
                
        return res
