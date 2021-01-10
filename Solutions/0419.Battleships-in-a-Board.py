"""
419. Battleships in a Board

Given an 2D board, count how many battleships are in it. 
The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. 
In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
"""
        
        
class UnionFind:
    
    def __init__(self):
        self.father = defaultdict(int)
        self.cnt = 0
        
    def add(self, x):
        if x not in self.father:
            self.father[x] = x
            self.cnt += 1
    
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]
    
    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt -= 1
            
            
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        uf = UnionFind()
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    uf.add((i, j))
                    for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        next_i, next_j = i + delta_i, j + delta_j
                        if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] == "X":
                            if (next_i, next_j) in uf.father:
                                uf.union((i, j), (next_i, next_j))
        return uf.cnt


"""
solutoin 2: O(1) space solution
whenever we meet a "X", we check if it is the top left corner of a battleship,
if it is cnt += 1
"""
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    if i - 1 >= 0 and board[i-1][j] == "X":  # check if (i, j) is the top left corner of a battleship
                        continue
                    if j - 1 >= 0 and board[i][j-1] == "X":
                        continue
                    cnt += 1
        return cnt
