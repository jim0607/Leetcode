"""
529. Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

 

Note:

The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
The input board won't be a stage when game is over (some mines have been revealed).
For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.
"""



"""
in dfs: step 1: check how many MINES are there in adjacent to (curr_i, curr_j);
step 2: based on adj_mine, we choose either continue dfs or stop
"""
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(curr_i, curr_j):
            adj_mine = 0        # check how many MINES are there in adjacent to (curr_i, curr_j)
            for delta_i, delta_j in [(1,0),(1,-1),(1,1),(0,1),(0,-1),(-1,1),(-1,-1),(-1,0)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if board[next_i][next_j] == "M":
                        adj_mine += 1
            
            # based on adj_mine, we choose either continue dfs or stop
            if adj_mine > 0:            # if adj_mine > 0, change to the number and stop dfs
                board[curr_i][curr_j] = str(adj_mine)
            elif adj_mine == 0:         # if adj_mine == 0, change curr_pos to "B" and continue dfs
                board[curr_i][curr_j] = "B"
                for delta_i, delta_j in [(1,0),(1,-1),(1,1),(0,1),(0,-1),(-1,1),(-1,-1),(-1,0)]:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < m and 0 <= next_j < n:
                        if board[next_i][next_j] == "E":
                            dfs(next_i, next_j)
        
        
        m, n = len(board), len(board[0])
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        if board[click[0]][click[1]] == "E":
            dfs(click[0], click[1])
            return board








class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
        elif board[click[0]][click[1]] == "E":
            visited = set()
            visited.add(tuple(click))
            self._dfs(board, click, visited)
            
        return board
        
    def _dfs(self, board, curr_pos, visited):
        moves = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        m, n = len(board), len(board[0])
        
        # 第一个for循环，更新board[curr_pos], 因为如果board[curr_pos].isdigit()就不能further explore了,
        adjacent_mine = 0
        for delta_x, delta_y in moves:
            next_x, next_y = curr_pos[0] + delta_x, curr_pos[1] + delta_y
            if 0 <= next_x < m and 0 <= next_y < n:
                if (next_x, next_y) not in visited:
                    if board[next_x][next_y] == "M":
                        adjacent_mine += 1
                        
        if adjacent_mine > 0:
            board[curr_pos[0]][curr_pos[1]] = str(adjacent_mine)
            return          # a digit act like a block and prevents further explore
            
        # 第二个for循环further explore
        board[curr_pos[0]][curr_pos[1]] = "B" 
        for delta_x, delta_y in moves:
            next_x, next_y = curr_pos[0] + delta_x, curr_pos[1] + delta_y
            if 0 <= next_x < m and 0 <= next_y < n:
                if (next_x, next_y) not in visited:
                    if board[next_x][next_y] == "E" or board[next_x][next_y] == "B":
                        visited.add((next_x, next_y))
                        self._dfs(board, (next_x, next_y), visited)
