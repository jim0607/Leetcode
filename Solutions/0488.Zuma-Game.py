"""
488. Zuma Game

Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). 
You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). 
Then, if there is a group of 3 or more balls in the same color touching, remove these balls. 
Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Example 1:

Input: board = "WRRBBW", hand = "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
Example 2:

Input: board = "WWRRBBWW", hand = "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
Example 3:

Input: board = "G", hand = "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 
Example 4:

Input: board = "RBYYBBRRB", hand = "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 
 
Constraints:

You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
1 <= board.length <= 16
1 <= hand.length <= 5
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
"""



"""
Each crushed board is a node in backtrack.
"""
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def backtrack(curr_board, curr_cnt):
            if len(curr_board) == 0:
                self.min_res = min(self.min_res, curr_cnt)
                return
            
            if not cnter:       # pruning - early stop  
                return
            
            lens = len(curr_board)
            for i in range(lens + 1):
                for ch in "RYBGW":
                    if cnter[ch] >= 1:
                        next_board = curr_board[:i] + ch + curr_board[i:]
                        next_board = crush(next_board)
                        cnter[ch] -= 1
                        if cnter[ch] == 0:
                            del cnter[ch]
                        backtrack(next_board, curr_cnt + 1)
                        cnter[ch] += 1
            
            
        def crush(s):
            """
            crush if there are 3 consecutive same chars. "WBBRRRBW" --> "WW".
            similar with 723. Candy Crush, we do it recurssively
            """
            res = ""
            need_to_crush = False
            for i, ch in enumerate(s):
                j = i + 1
                while j < len(s) and s[j] == ch:
                    j += 1
                if j - i >= 3:
                    res = s[:i] + s[j:]
                    need_to_crush = True
                    break
                    
            if not need_to_crush:
                return s

            return crush(res)
        
        
        cnter = collections.Counter(hand)
        self.min_res = float("inf")
        backtrack(board, 0)
        return -1 if self.min_res == float("inf") else self.min_res
