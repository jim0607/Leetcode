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
step 2: union one-by-one, until (0, 0) and (m-1, n-1) are connected
算法其实有一点点类似Krusal求MST
"""
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        positions = [(i, j) for i in range(m) for j in range(n)]    # 定义一个一维数组， 注意python是怎么写的
        positions.sort(key = lambda x: -A[x[0]][x[1]])      # O(MNlogMN)
        
        uf = UnionFind(positions)
        
        visited = set()
        for pos in positions:
            visited.add(pos)
            
            i, j = pos[0], pos[1]
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                adj_i, adj_j = i + delta_i, j + delta_j
                if 0 <= adj_i < m and 0 <= adj_j < n:       # 这里要判断不要out of bound
                    # 注意nextPoint一定要in visited才能将其连上currPoint!! 这是UnionFind的定义决定的
                    # 只有visited过了才可以连接起来，因为visited过的一定是比现在point大的，我们只连大的
                    # 如果没有visited过的就去连上，那么会连上很多小的，比如例子中7会连上1
                    if (adj_i, adj_j) in visited:
                        uf.union((i, j), (adj_i, adj_j))
                    
            if uf.connected((0, 0), (m-1, n-1)):     # check if (0, 0) and (m-1, n-1) are connected
                return A[i][j]    # if connected, then return current position cuz it is the minimum in the path
            

class UnionFind:
    
    def __init__(self, positions):
        self.father = collections.defaultdict(tuple)
        
        for pos in positions:
            self.add(pos)
                
    def add(self, x):
        self.father[x] = x
        
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def connected(self, a, b):
        return self.find(a) == self.find(b)
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
