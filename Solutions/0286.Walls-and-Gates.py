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
    EMPTY = 2147483647
    MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:
            return rooms
        
        self.bfs(rooms)
        
    def bfs(self, rooms):
        """change all the "INF" to a value that equals the layer number"""
        
        m, n = len(rooms), len(rooms[0])
        q = collections.deque()
        visited = set()
        for i in range(m):      # add the first layer to the q
            for j in range(n):
                if rooms[i][j] == self.GATE:
                    q.append((i, j))
                    visited.add((i, j))     # 一对孪生兄弟
        
        distance = 0
        while q:
            distance += 1
            lens = len(q)
            for _ in range(lens):       # 必须要层序遍历，否则就不对，一定要理解为什么层序遍历才能保证每次INF都能变成最小距离
                (x, y) = q.popleft()
                for delta_x, delta_y in self.MOVES:
                    neighbor_x, neighbor_y = x + delta_x, y + delta_y
                    if self.inBound(rooms, neighbor_x, neighbor_y) and rooms[neighbor_x][neighbor_y] == self.EMPTY and (neighbor_x, neighbor_y) not in visited:
                        rooms[neighbor_x][neighbor_y] = distance
                        q.append((neighbor_x, neighbor_y))
                    
    def inBound(self, rooms, x, y):
        m, n = len(rooms), len(rooms[0])
        if 0 <= x < m and 0 <= y < n:
            return True

        return False
