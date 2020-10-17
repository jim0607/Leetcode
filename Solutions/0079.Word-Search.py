"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


"""
图上的搜索：dfs + backtracking
这题5min内写出来了才算真正会了图上的dfs + backtracking
Time Complexity: O(N*4^L) where N is the number of cells in the board and L is the length of the word to be matched.
"""
"""
套用backtrack的模板，backtrack 里面要传入(curr_i, curr_j, curr_idx on word). find solution: if board[next_i][next_j] == word[curr_idx + 1].  
if find a solution, backtrack函数输出True
if valid: if board[next_i][next_j] == word[curr_idx + 1]. 需要一个visited set来标记已经走过的路径避免走重复的路径。
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(curr_i, curr_j, curr_idx):
            if curr_idx == len(word) - 1:
                return True
            for delta_i, delta_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if (next_i, next_j) not in visited:
                        if board[next_i][next_j] == word[curr_idx + 1]:
                            visited.add((next_i, next_j))
                            if backtrack(next_i, next_j, curr_idx + 1):
                                return True
                            visited.remove((next_i, next_j))        # backtrack
            return False
        
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:    # trigger a bbacktrack search whenever we find a char == word[0]
                    visited = set()
                    visited.add((i, j))
                    if backtrack(i, j, 0):
                        return True
        return False









class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 1 and len(word) == 1 and board[0][0] == word[0]:
            return True
        
        self.board = board    # 尽量少传一些东西到backtrack function
        self.MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.res = False
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == word[0]:   # trigger a dfs whenever we find a char == word[0]
                    self.visited = set()
                    self.visited.add((i, j))
                    self.backtrack(i, j, word, 1)
                    
                if self.res:        # 如果找到直接return True
                    return True
                
        return False
    
    def backtrack(self, i, j, word, currIdx):   # 套用doc里的模板，想想递归的定义
        if currIdx == len(word):
            self.res = True
            return

        for delta_x, delta_y in self.MOVES:
            new_x, new_y = i + delta_x, j + delta_y
            
            if new_x < 0 or new_x >= len(self.board) or new_y < 0 or new_y >= len(self.board[0]):
                continue
            if (new_x, new_y) in self.visited:
                continue
            if self.board[new_x][new_y] != word[currIdx]:
                continue
                
            currIdx += 1
            self.visited.add((new_x, new_y))
            self.backtrack(new_x, new_y, word, currIdx)
            if self.res:    # 这样就不用再去找其他的n三个ext_x, next_y了，节约了一点时间，这样才通过的，没有这句话就TLE
                return 
            currIdx -= 1
            self.visited.remove((new_x, new_y))
