"""
1138. Alphabet Board Path

On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.

Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:

Input: target = "code"
Output: "RR!DDRR!UUL!R!"
"""



"""
mapping: ch --> idx in board.
each time we start from target[i] and do bfs to find target[i+1].
"""
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        mapping = defaultdict(tuple)   # ch --> the pos of the ch
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        for i, s in enumerate(board):
            for j, ch in enumerate(s):
                mapping[ch] = (i, j)
        
        directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        
        res = ""
        start_ch = "a"
        for ch in target:
            res += self.find_path(start_ch, ch, mapping, directions)
            start_ch = ch
        return res
    
    def find_path(self, start_ch, end_ch, mapping, directions):
        start_pos, end_pos = mapping[start_ch], mapping[end_ch]
        
        q = deque()
        visited = set()
        q.append((start_pos[0], start_pos[1], ""))
        visited.add(start_pos)
        
        while len(q) > 0:
            lens = len(q)
            for _ in range(lens):
                curr_i, curr_j, curr_path = q.popleft()
                if (curr_i, curr_j) == end_pos:
                    return curr_path + "!"
                
                for direction, (delta_i, delta_j) in directions.items():
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < 5 and 0 <= next_j < 5 or (next_i == 5 and next_j == 0):
                        if (next_i, next_j) not in visited:
                            q.append((next_i, next_j, curr_path + direction))
                            visited.add((next_i, next_j))
