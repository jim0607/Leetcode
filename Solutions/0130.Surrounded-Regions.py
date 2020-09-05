"""130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""



"""
We do dfs for all "O" on the boarder. And store them in visited.  Every node in visited 
is not surrounded by "X" because it is connected to the boarder.
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board
        
        # step 1: put all "O" connected with board into a set
        m, n = len(board), len(board[0])
        visited = set()     # store all the "O" that are connected with board
        for i in range(m):
            if board[i][0] == "O" and (i, 0) not in visited:
                self._dfs(board, i, 0, visited)
            if board[i][n-1] == "O" and (i, n-1) not in visited:
                self._dfs(board, i, n-1, visited)
        for j in range(n):
            if board[0][j] == "O" and (0, j) not in visited:
                self._dfs(board, 0, j, visited)
            if board[m-1][j] == "O" and (m-1, j) not in visited:
                self._dfs(board, m-1, j, visited)
               
        # step 2: traverse the matrix again to switch "O" that are not connected with board
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"                
    
    def _dfs(self, board, curr_i, curr_j, visited):
        visited.add((curr_i, curr_j))
        for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_i, next_j = curr_i + delta_i, curr_j + delta_j
            if 0 <= next_i < len(board) and 0 <= next_j < len(board[0]):
                if board[next_i][next_j] == "O":
                    if (next_i, next_j) not in visited:
                        self._dfs(board, next_i, next_j, visited)



"""
Solutino 1: Union Find
Step 1: Union all the "O" that are neighborign with each other. We do a weighted union, meaning when we union, we also choose to point to the one that is on the border.
Step 2: 2nd pass, we change to "X" tha "O" that has a root not on border.
"""

def on_border(i, j, grid):
    m, n = len(grid), len(grid[0])
    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
        return True

    return False


class UnionFind:

    def __init__(self, grid):
        self.father = collections.defaultdict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O":
                    self.father[(i, j)] = (i, j)

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, a, b, grid):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            if on_border(root_b[0], root_b[1], grid):       # debug了好久发现这里应该是判断root_b的位置而不是b
                self.father[root_a] = root_b
            else:
                self.father[root_b] = root_a


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board

        uf = UnionFind(board)

        visited = set()
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in visited:
                    visited.add((i, j))
                    for move in moves:
                        neighbor_i, neighbor_j = i + move[0], j + move[1]
                        if 0 <= neighbor_i < m and 0 <= neighbor_j < n and \
                                board[neighbor_i][neighbor_j] == "O" and \
                                (neighbor_i, neighbor_j) not in visited:
                            uf.union((i, j), (neighbor_i, neighbor_j), board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    root = uf.find((i, j))
                    if not on_border(root[0], root[1], board):
                        board[i][j] = "X"
                        
                        
                        
"""
Solution 2: bfs
Step 1: Start from border, do a bfs for "O", mark all the "O" that can be reached from the border.
We can either mark by putting them into a visited set, or just change it to some symbol "#".
Step 2: 2nd pass, we change to "X" tha "O" that could not be visited from the border.
"""
class Solution:
    def solve(self, grid) -> None:
        if not grid or not grid[0]:
            return grid
        
        m, n = len(grid), len(grid[0])
        
        self.visited = set()
        for i in range(m):
            for j in range(n):
                if 0 < i < m - 1 and 0 < j < n - 1:     # if not on border, we skip. we only do bfs for "O" on border
                    continue
                if grid[i][j] != "O":
                    continue
                if (i, j) in self.visited:
                    continue
                    
                self.bfs(grid, i, j)
                
        for i in range(1, m - 1):
            for j in range(1, n -1):
                if grid[i][j] == "O" and (i, j) not in self.visited:
                    grid[i][j] = "X"
                    
    def bfs(self, grid, i, j):
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        
        q = collections.deque()
        q.append((i, j))
        self.visited.add((i, j))
        
        while q:
            curr_i, curr_j = q.popleft()
            for delta_i, delta_j in moves:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and \
                grid[next_i][next_j] == "O" and (next_i, next_j) not in self.visited:
                    q.append((next_i, next_j))
                    self.visited.add((next_i, next_j))
                    
                    
                    
"""
Solution 3: dfs 从bfs change 到dfs, 我们其实只改了一行q.popleft() 改成了 q.pop(), 这样就相当于当stack使用了
Step 1: Start from border, do a dfs for "O", mark all the "O" that can be reached from the border.
We can either mark by putting them into a visited set, or just change it to some symbol "#".
Step 2: 2nd pass, we change to "X" tha "O" that could not be visited from the border.
"""
class Solution:
    def solve(self, grid) -> None:
        if not grid or not grid[0]:
            return grid
        
        m, n = len(grid), len(grid[0])
        
        self.visited = set()
        for i in range(m):
            for j in range(n):
                if 0 < i < m - 1 and 0 < j < n - 1:     # if not on border, we skip. we only do bfs for "O" on border
                    continue
                if grid[i][j] != "O":
                    continue
                if (i, j) in self.visited:
                    continue
                    
                self.dfs(grid, i, j)
                
        for i in range(1, m - 1):
            for j in range(1, n -1):
                if grid[i][j] == "O" and (i, j) not in self.visited:
                    grid[i][j] = "X"
                    
    def dfs(self, grid, i, j):
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        
        q = collections.deque()
        q.append((i, j))
        self.visited.add((i, j))
        
        while q:
            curr_i, curr_j = q.pop()        # this is the only change from bfs to dfs, we use a stack instead of a q
            for delta_i, delta_j in moves:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and \
                grid[next_i][next_j] == "O" and (next_i, next_j) not in self.visited:
                    q.append((next_i, next_j))
                    self.visited.add((next_i, next_j))
                  
