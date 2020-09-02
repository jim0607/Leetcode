You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4


class Solution:
    WALL = -1
    GATE = 0
    EMPTY = 2**31 - 1
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify grid in-place instead.
        """
        if not grid or not grid[0]:
            return grid
        
        # step 1: add the first layer to q
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == self.GATE:
                    q.append((i, j))
      
        # step 2: bfs layer by layer and update grid in-place
        dist = 0
        while len(q) > 0:
            dist += 1
            lens = len(q)
            for _ in range(lens):
                curr_i, curr_j = q.popleft()
                for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < m and 0 <= next_j < n:
                        if grid[next_i][next_j] == self.EMPTY:
                            q.append((next_i, next_j))
                            grid[next_i][next_j] = dist
