Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

Example 1:

Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:

Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1


"""
solution 1: Time: O(MN)
"""
class Solution:
    WATER = 0
    LAND = 1
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        The max distance is the max steps to change all WATER to LAND. So we firslty put all land in a q,
        than do bfs layer by layer to change WATER to LAND in-place. Time: O(MN)
        """
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.LAND:
                    q.append((i, j))
        dist = -1
        while len(q) > 0:
            dist += 1
            lens = len(q)
            for _ in range(lens):
                curr_i, curr_j = q.popleft()
                for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < m and 0 <= next_j < n:
                        if grid[next_i][next_j] == self.WATER:
                            q.append((next_i, next_j))
                            grid[next_i][next_j] = self.LAND   # 直接in-place修改，就不需要visited了
                            
        return dist if dist > 0 else -1
       
       
"""
The below solution is trigger a bfs at each WATER - TLE cuz Time: O(M^2N^2)
"""
class Solution:
    WATER = 0
    LAND = 1
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_dist = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.WATER:
                    max_dist = max(max_dist, self._bfs(grid, i, j))
        return max_dist
    
    def _bfs(self, grid, i, j):
        q = collections.deque()
        visited = set()
        q.append((i, j))
        visited.add((i, j))
        
        dist = -1
        while len(q) > 0:
            dist += 1
            lens = len(q)
            for _ in range(lens):
                curr_i, curr_j = q.popleft()
                if grid[curr_i][curr_j] == self.LAND:
                    return dist
                for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]):
                        if (next_i, next_j) not in visited:
                            q.append((next_i, next_j))
                            visited.add((next_i, next_j))
        return -1
