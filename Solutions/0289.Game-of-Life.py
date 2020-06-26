289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?


"""
O(MN), O(MN) solution
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        m, n = len(board), len(board[0])
        
        # copy_board = board.copy()   why using a deep copy here is not correct, because .copy() is a shallow copy.
        # for a shallow copy of a 2D list, changing the orignal one will affect the copied one, 
        # and changing the copied one will also affect the orignal one.
        copy_board = [[board[i][j] for j in range(n)] for i in range(m)]    # this line is actually implmenting a deep copy 

        for i in range(m):
            for j in range(n):
                cnt_live = 0
                for delta_i, delta_j in neighbors:
                    neighbor_i, neighbor_j = i + delta_i, j + delta_j
                    if 0 <= neighbor_i < m and 0 <= neighbor_j < n:
                        if copy_board[neighbor_i][neighbor_j] == 1:
                            cnt_live += 1
                
                # print(cnt_live)
                if copy_board[i][j] == 1:
                    if cnt_live < 2 or cnt_live > 3:
                        board[i][j] = 0
                
                elif copy_board[i][j] == 0:
                    if cnt_live == 3:
                        board[i][j] = 1
    
"""
Folllow up 1:
Could you solve it in-place? Remember that the board needs to be updated at the same time: 
You cannot update some cells first and then use their updated values to update other cells.
"""    
"""
"""
O(MN) O(1) solution.
Two traversals. Traversal 1: dead -> live: mark as 2; live -> dead: -1  can be whatever number you want, it's just for mark.
Traversal 2: re-mark 2 to 1, -1 to 0
"""
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                cnt_live = 0
                for delta_i, delta_j in neighbors:
                    neighbor_i, neighbor_j = i + delta_i, j + delta_j
                    if 0 <= neighbor_i < m and 0 <= neighbor_j < n:
                        if board[neighbor_i][neighbor_j] == 1 or board[neighbor_i][neighbor_j] == 2:
                            cnt_live += 1
                if board[i][j] == 0:
                    if cnt_live == 3:
                        board[i][j] = -1
                if board[i][j] == 1:
                    if cnt_live < 2 or cnt_live > 3:
                        board[i][j] = 2
                        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0

"""             
Follow up 2:
In this question, we represent the board using a 2D array. In principle, the board is infinite, 
which would cause problems when the active area encroaches the border of the array. How would you address these problems?

Such open ended problems are better suited to design discussions during programming interviews and 
it's a good habit to take into consideration the scalability aspect of the problem since your interviewer might be interested in talking about such problems. 
The discussion section already does a great job at addressing this specific portion of the problem. 
We will briefly go over two different solutions that have been provided in the discussion sections, as they broadly cover two main scenarios of this problem.
It's quite possible that we have a gigantic matrix with a very few live cells. In that case it would be stupidity to save the entire board as is.
If we have an extremely sparse matrix, it would make much more sense to actually save the location of only the live cells 
and then apply the 4 rules accordingly using only these live cells.
Essentially, we obtain only the live cells from the entire board and then apply the different rules using only the live cells and finally we update the board in-place. 
The only problem with this solution would be when the entire board cannot fit into memory. 
If that is indeed the case, then we would have to approach this problem in a different way. 
For that scenario, we assume that the contents of the matrix are stored in a file, one row at a time.
In order for us to update a particular cell, we only have to look at its 8 neighbors which essentially lie in the row above and below it. 
So, for updating the cells of a row, we just need the row above and the row below. Thus, we read one row at a time from the file and at max we will have 3 rows in memory. 
We will keep discarding rows that are processed and then we will keep reading new rows from the file, one at a time.
"""
