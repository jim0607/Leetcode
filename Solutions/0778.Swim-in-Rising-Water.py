778. Swim in Rising Water

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.



"""
find a path with the minimum max-height in the path.
采用Dikstra, heapq中存放(curr_max_val, curr_node). 每次pop出来的都是min height就可了 - O(N^2*log(N^2)), where N is the lens of grid.
"""

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        hq = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))   # 注意做Min of maximum or max of minimum的题目都需要visited set的
       
        while len(hq) > 0:
            curr_max_val, curr_i, curr_j = heappop(hq)   # 每次pop出来的都是最小的max_val
            
            if (curr_i, curr_j) == (m-1, n-1):
                return curr_max_val
            
            for delta_i, delta_j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if (next_i, next_j) not in visited:
                        next_val = grid[next_i][next_j]
                        heappush(hq, (max(curr_max_val, next_val), next_i, next_j))
                        visited.add((next_i, next_j))       # 别忘了一对孪生兄弟
    
    

"""
Solution 2: Union-Find
step 1: sort the array by the values asccendingly
step 2: union one-by-one, until (0, 0) and (m-1, n-1) are connected
算法其实有一点点类似Krusal求MST
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        position = [(i, j) for i in range(m) for j in range(n)]
        position.sort(key = lambda x: grid[x[0]][x[1]])     # step 1: sort the position list by the values asccendingly
        
        uf = UnionFind(position)
        
        visited = set()
        for i, j in position:     # step 2: union one-by-one, until (0, 0) and (m-1, n-1) are connected
            visited.add((i, j))
            
            for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                adj_i, adj_j = i + delta_i, j + delta_j
                if (adj_i, adj_j) in visited:   # ****注意nextPoint一定要in visited才能将其连上currPoint!!
                    uf.union((i, j), (adj_i, adj_j))
                    
            if uf.connected((0, 0), (m-1, n-1)):    # check if (0, 0) and (m-1, n-1) are connected
                return grid[i][j]      # if connected, then return current position cuz it is the maximum in the path  
        
        
class UnionFind:
    
    def __init__(self, position):
        self.father = collections.defaultdict(tuple)
        
        for pos in position:
            self.father[pos] = pos
            
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]    
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
    
    def connected(self, a, b):
        return self.find(a) == self.find(b)
