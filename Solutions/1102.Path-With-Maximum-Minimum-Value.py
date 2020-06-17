1102. Path With Maximum Minimum Value

Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).


Example 1:

Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: 
The path with the maximum score is highlighted in yellow. 
Example 2:

Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:

Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3


"""
Solution 1: Dijkstra's : 每次都把目前为止最小值最大的那个path的那个cueeNode pop出来，从那个currNode开始往后走
maintain a heapq to store (the minimum value in the path so far till the currPos, currPos)
each time, we push (min(nextVal, currMinVal), nextPos)
O(MNlogMN), O(MN)
"""
from heapq import *
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(A), len(A[0])
        
        hq = []
        heappush(hq, (-A[0][0], (0, 0)))
        visited = set()
        visited.add((0, 0))
        
        while hq:
            currMin, currPos = heappop(hq)
            if currPos == (m-1, n-1):
                return -currMin
            
            for move in moves:
                nextPos = (currPos[0] + move[0], currPos[1] + move[1])
                if nextPos[0] < 0 or nextPos[0] >= m or nextPos[1] < 0 or nextPos[1] >= n:
                    continue
                if nextPos in visited:
                    continue
                    
                heappush(hq, (-min(-currMin, A[nextPos[0]][nextPos[1]]), nextPos))
                visited.add(nextPos)

                
                
"""
Solution 2: Union-Find
step 1: sort the array by the values descendingly
step 2: union one-by-one, until (0, 0) and (m-1, n-1) is connected
"""
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(A), len(A[0])
        
        points = [(x, y) for x in range(m) for y in range(n)]   # 定义一个一维数组， 注意python是怎么写的
        points.sort(key = lambda point: -A[point[0]][point[1]])     # O(MNlogMN)
        
        graph = UnionFind(points)
        
        visited = set()
        for point in points:        # O(MN)
            visited.add(point)
            
            for move in moves:
                nextPoint = (point[0] + move[0], point[1] + move[1])
                if nextPoint[0] < 0 or nextPoint[0] >= m or nextPoint[1] < 0 or nextPoint[1] >= n:
                    continue
                if nextPoint in visited:   # 注意nextPoint一定要in visited才能将其连上currPoint!! 这是UnionFind的定义决定的
                    graph.union(point, nextPoint)
                
            if graph.find((0, 0)) == graph.find((m-1, n-1)):    # check if (0, 0) and (m-1, n-1) are connected
                return A[point[0]][point[1]]


class UnionFind:
    def __init__(self, points):
        self.father = collections.defaultdict()
        for point in points:
            self.father[point] = point
        
    def add(self, item):
        self.father[item] = item
        
    def find(self, item):
        if self.father[item] == item:
            return item
        
        self.father[item] = self.find(self.father[item])
        
        return self.father[item]
        
    def union(self, item1, item2):
        root1, root2 = self.find(item1), self.find(item2)
        if root1 != root2:
            self.father[root1] = root2