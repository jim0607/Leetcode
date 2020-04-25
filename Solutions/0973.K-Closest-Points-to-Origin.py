973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].



"""以squre来构建heap就可以了，heap中的元素是(square, point)
O(NlogN)"""

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            sqr = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(heap, (sqr, point))
        
        res = []
        for _ in range(K):
            res.append(heapq.heappop(heap)[1])
            
        return res

# the following solution is just to sort, easy to think.
# O(NlogN)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda x: (x[0]**2 + x[1]**2))
        
        res = []
        for i in range(K):
            res.append(points[i])
            
        return res
