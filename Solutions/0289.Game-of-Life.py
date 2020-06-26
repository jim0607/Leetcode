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
