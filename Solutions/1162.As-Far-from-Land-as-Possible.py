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



"""bfs: the maximum distance is steps needed to change all water to be land """
class Solution:
    
    WATER = 0
    LAND = 1
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        the max distance is the max steps to change all water to land
        so we firslty put all land in a q
        than pop them out one by one and at hte same time change adjacent water into land, append into q
        """
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.LAND:
                    q.append((i, j))
                    visited.add((i, j))
            
        steps = -1
        while q:
            lens = len(q)
            steps += 1
            
            for _ in range(lens):
                curr_x, curr_y = q.popleft()
                
                for move in self.MOVES:
                    next_x, next_y = curr_x + move[0], curr_y + move[1]
                    if 0 <= next_x < m and 0 <= next_y < n and \
                    grid[next_x][next_y] == self.WATER and \
                    (next_x, next_y) not in visited:
                        grid[next_x][next_y] = self.LAND
                        q.append((next_x, next_y))
                        visited.add((next_x, next_y))
                        
        return steps if steps > 0 else -1
