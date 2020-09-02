695. Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

"""
dfs version
"""
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_cnt = 0
        visited = set()     # 也可以不用visited, 而是就地修改grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if (i, j) in visited:
                        continue
                    cnt = self._dfs(grid, i, j, visited)
                    max_cnt = max(max_cnt, cnt)
        return max_cnt
    
    def _dfs(self, grid, i, j, visited):
        visited.add((i, j))
        cnt = 1
        for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_i, next_j = i + delta_i, j + delta_j
            if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]):
                if grid[next_i][next_j] == 1:
                    if (next_i, next_j) not in visited:
                        cnt += self._dfs(grid, next_i, next_j, visited)
        return cnt


"""
bfs version
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        self.visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    res = max(res, self.bfs(grid, i, j))
                    
        return res
    
    def bfs(self, grid, i, j):
        q = collections.deque()
        q.append((i, j))
        self.visited.add((i, j))

        cnt = 0
        while q:
            curr_x, curr_y = q.popleft()
            cnt += 1

            for delta_x, delta_y in self.MOVES:
                next_x, next_y = delta_x + curr_x, delta_y + curr_y

                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and \
                grid[next_x][next_y] == 1 and (next_x, next_y) not in self.visited:
                    q.append((next_x, next_y))
                    self.visited.add((next_x, next_y))

        return cnt
