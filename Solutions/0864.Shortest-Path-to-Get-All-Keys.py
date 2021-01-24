"""
864. Shortest Path to Get All Keys

We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  
We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  
This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.

Example 1:

Input: ["@.a.#","###.#","b.A.B"]
Output: 8
Example 2:

Input: ["@..aA","..B#.","....b"]
Output: 6
"""


"""
BFS algorithm can be used to solve a lot of problems of finding shortest distance.
In this problem, we may visit a point more than one times, simply storing visited position is not enough.
We need to save (pos, keys_collected) in the visited set, because visiting the same pos without getting new key is not allowed,
but in order to get a new key, we may visit a certain pos, after getting the key, we may go back and visit the pos again.
"""
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        keys_collected = tuple()  # cannot use mutable data types like set or list, 
                     # because they are unhashable and thus cannot add into visited set, so here we use a tuple instead
        visited = set()
        total_keys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    q.append((i, j, keys_collected))
                    visited.add((i, j, keys_collected))
                if grid[i][j].islower():
                    total_keys += 1
                    
        steps = -1 
        while len(q) > 0:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr_i, curr_j, curr_keys_collected = q.popleft()
                if len(curr_keys_collected) == total_keys:          # 如果collect all keys, then return
                    return steps
                
                for delta_i, delta_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < m and 0 <= next_j < n:
                        if grid[next_i][next_j] == '#':         # if it's a WALL, then we can not go through
                            continue
                            
                        if grid[next_i][next_j] == "." or grid[next_i][next_j] == "@":
                            if (next_i, next_j, curr_keys_collected) not in visited:
                                q.append((next_i, next_j, curr_keys_collected))
                                visited.add((next_i, next_j, curr_keys_collected))
                                
                        if grid[next_i][next_j].isupper():      # if it's a lock, we can go though it only if we have the key collected already       
                            if grid[next_i][next_j].lower() not in curr_keys_collected:     # if the key is not collected already, we cannot go through
                                continue
                            if (next_i, next_j, curr_keys_collected) not in visited:
                                q.append((next_i, next_j, curr_keys_collected))
                                visited.add((next_i, next_j, curr_keys_collected))                                
                                
                        if grid[next_i][next_j].islower():      # if it's a key, then we need to update the key_collected 
                            if (next_i, next_j, curr_keys_collected) not in visited: 
                                next_keys_collected_set = set(curr_keys_collected)      # 注意我们需要用tuple cuz set is mutable, so not hashable
                                next_keys_collected_set.add(grid[next_i][next_j])
                                next_keys_collected = tuple(next_keys_collected_set)
                                q.append((next_i, next_j, next_keys_collected))
                                visited.add((next_i, next_j, next_keys_collected))
                            
        return -1
