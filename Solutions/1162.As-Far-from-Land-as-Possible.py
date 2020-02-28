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



"""bfs: the maximum distance is steps needed to change all "0" to be "1" """
class Solution:
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        q = collections.deque()
        visited = set()
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    visited.add((i, j))
                    
        steps = -1
        while q:
            steps += 1
            lens = len(q)
            
            for _ in range(lens):
                (x, y) = q.popleft()
                for delta_x, delta_y in self.MOVES:
                    neighbor_x, neighbor_y = x + delta_x, y + delta_y
                    if self.inBound(grid, neighbor_x, neighbor_y) and grid[neighbor_x][neighbor_y] == 0 and (neighbor_x, neighbor_y) not in visited:
                        q.append((neighbor_x, neighbor_y))
                        visited.add((neighbor_x, neighbor_y))
        
        return -1 if steps == 0 else steps
                        
    def inBound(self, grid, x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return True
        
        return False
