348. Design Tic-Tac-Toe

Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?


Follow up:
Could you do better than O(n2) per move() operation?




"""
just use a two lists to record how many are needed at each row and each col for player1.
same for player 2. 
"""
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.col_need1 = [n for _ in range(n)]
        self.row_need1 = [n for _ in range(n)]
        self.left_diag_need1 = n
        self.right_diag_need1 = n
        self.col_need2 = [n for _ in range(n)]
        self.row_need2 = [n for _ in range(n)]
        self.left_diag_need2 = n
        self.right_diag_need2 = n
        
        self.finished = False
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if self.finished:
            return -1
        
        if player == 1:
            self.row_need1[row] -= 1
            if self.row_need1[row] == 0:
                self.finished = True
                return 1
            self.col_need1[col] -= 1
            if self.col_need1[col] == 0:
                self.finished = True
                return 1
            if row == col:
                self.left_diag_need1 -= 1
                if self.left_diag_need1 == 0:
                    self.finished = True
                    return 1
            if row + col == self.n - 1:
                self.right_diag_need1 -= 1
                if self.right_diag_need1 == 0:
                    self.finished = True
                    return 1
                    
        if player == 2:
            self.row_need2[row] -= 1
            if self.row_need2[row] == 0:
                self.finished = True
                return 2
            self.col_need2[col] -= 1
            if self.col_need2[col] == 0:
                self.finished = True
                return 2
            if row == col:
                self.left_diag_need2 -= 1
                if self.left_diag_need2 == 0:
                    self.finished = True
                    return 2
            if row + col == self.n - 1:
                self.right_diag_need2 -= 1
                if self.right_diag_need2 == 0:
                    self.finished = True
                    return 2
                
        return 0




"""
same idea as above, different implementation.
use a hashmap for player1: key is row/col/dia, val is how many taken by player1 at row/col/dia; use another hashmap for player 2. 
then each time we place a position, we update the hashmap, which takes O(1)
"""
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.finished = False
        self.player1 = collections.defaultdict(int) # key is row/col/dia, val is how many taken by player1 at row/col/dia
        self.player2 = collections.defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if self.finished:   # if game is finished, we stop the game
            return
        
        if player == 1:
            self.player1[row+0.5] += 1
            self.player1[col+0.4] += 1
            if row == col:
                self.player1[-1] += 1    # -1 means one diagonal
            if row + col == self.n - 1:
                self.player1[-2] += 1
            if self.player1[row+0.5] == self.n or self.player1[col+0.4] == self.n or self.player1[-1] == self.n or self.player1[-2] == self.n:
                self.finished = True
                return 1
            
        if player == 2:
            self.player2[row+0.5] += 1    # 这里给row加个0.5, 给col加个0.4是为了避免row和col重复的情况，也可以把row的hashmap和col的hashmap分开
            self.player2[col+0.4] += 1
            if row == col:
                self.player2[-1] += 1    # -1 means one diagonal
            if row + col == self.n - 1:
                self.player2[-2] += 1    # -2 means another diagonal
            if self.player2[row+0.5] == self.n or self.player2[col+0.4] == self.n or self.player2[-1] == self.n or self.player2[-2] == self.n:
                self.finished = True
                return 2
            
        if not self.finished:
            return 0
            
        # total = 0
        # for key, cnt in self.player1.items():
        #     total += cnt if (key != -1 and key != -2) else 0
        # if total == self.n ** 2:        # if no one can win
        #     self.finished = True
        #     return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
