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
Solution 1: Dijkstra's : 
我们要的是path里面的最大的最小值, 所以我们把每个path里面的最小值放入max heap, 这样我们每次pop出来的都是path里面最大的那个最小值
每次都把目前为止最小值最大的那个path的那个cueeNode pop出来，从那个currNode开始往后走
maintain a heapq to store (the minimum value in the path so far till the currPos, currPos)
each time, we push (min(nextVal, currMinVal), nextPos)
O(MNlogMN), O(MN)
"""
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        hq = [(-grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))      # 注意做Min of maximum or max of minimum的题目都需要visited set的
        while len(hq) > 0:
            curr_min_val, curr_i, curr_j = heappop(hq)      # 每次pop出来的都是path里面最大的那个最小值
            curr_min_val = -curr_min_val    # curr_min_val stands for the curr max score of path so far
            
            if (curr_i, curr_j) == (m-1, n-1):
                return curr_min_val
            
            for delta_i, delta_j in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if (next_i, next_j) not in visited:
                        next_val = grid[next_i][next_j]
                        heappush(hq, (-min(next_val, curr_min_val), next_i, next_j))    # ***** 注意这里很容易错，
                        visited.add((next_i, next_j))       # 我们要的是path里面的最大的最小值, 所以我们把每个path里面的最小值放入max heap,              
                                                            # 这样我们每次pop出来的都是path里面最大的那个最小值

                
                
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
