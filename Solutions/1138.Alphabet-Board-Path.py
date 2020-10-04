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
        def bfs(start_pos, target_pos):
            q = collections.deque()
            visited = set()
            curr_path = ""
            q.append((start_pos, curr_path))
            visited.add(start_pos)
            while len(q) > 0:
                lens = len(q)
                for _ in range(lens):
                    (curr_i, curr_j), curr_path = q.popleft()
                    if (curr_i, curr_j) == target_pos:
                        curr_path += "!"
                        return curr_path
                    for dr, (delta_i, delta_j) in directions.items():
                        next_i, next_j = curr_i + delta_i, curr_j + delta_j
                        if (next_i, next_j) in mapping.values():
                            if (next_i, next_j) not in visited:
                                next_path = curr_path + dr
                                q.append(((next_i, next_j), next_path))
                                visited.add((next_i, next_j))

        
        mapping = {"a": (0, 0), "b": (0, 1), "c": (0, 2), "d": (0, 3), "e": (0, 4),
                   "f": (1, 0), "g": (1, 1), "h": (1, 2), "i": (1, 3), "j": (1, 4),
                   "k": (2, 0), "l": (2, 1), "m": (2, 2), "n": (2, 3), "o": (2, 4),
                   "p": (3, 0), "q": (3, 1), "r": (3, 2), "s": (3, 3), "t": (3, 4),
                   "u": (4, 0), "v": (4, 1), "w": (4, 2), "x": (4, 3), "y": (4, 4),
                   "z": (5, 0)}
        directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        res = ""
        start_pos = (0, 0)
        for target_ch in target:
            res += bfs(start_pos, mapping[target_ch])
            start_pos = mapping[target_ch]
        return res
