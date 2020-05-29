1091. Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

Example 1:

Input: [[0,1],[1,0]]

Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]

Output: 4

Note:
1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1




class Solution:
    MOVES = [(1, 0), (-1, 0), (1, 1), (-1, 1), (0, 1), (0, -1), (1, -1), (-1, -1)]
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        source = (0, 0)
        target = (m-1, n-1)
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        
        q = collections.deque()
        visited = set()
        q.append(source)
        visited.add(source)
        steps = 0
        while q:
            lens = len(q)
            steps += 1
            for _ in range(lens):
                curr_x, curr_y = q.popleft()
                if (curr_x, curr_y) == target:
                    return steps
                
                for delta_x, delta_y in self.MOVES:
                    next_x, next_y = curr_x + delta_x, curr_y + delta_y
                    if self.isNotValid(next_x, next_y, grid):
                        continue
                    if (next_x, next_y) in visited:
                        continue
                    q.append((next_x, next_y))
                    visited.add((next_x, next_y))
       
        return -1
    
    def isNotValid(self, x, y, grid):
        m, n = len(grid), len(grid[0])
        if x < 0 or x >= m or y < 0 or y >= n:
            return True
        if grid[x][y] == 1:
            return True
        
        return False
        
        
        
        
"""
If you need to find shortest path between just two points, then A* search shows better performance than bfs.
From implementation perspective it the same code just swapping the queue with a priority queue.
On each iteration you estimate minimum path to the goal by:
f((i,j))=g((i,j))+h((i,j))
Where:
g((i,j)) = shortest path length found so far from start to (i, j)
h((i,j)) = estimation to reach goal - bottom-right cell. For cell (i, j) it is calculated simply by max(m - i - 1, n - j - 1).
Important for A* search is that h((i,j)) does not overestimate the actual cost to get to the goal.
"""
