"""
980. Unique Paths III

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
"""


"""
套用backtrack模板就可以了. 每一个位置都有3种可能，所以time complexity O(3^N). 
"""
"""
backtrack结束条件：every non-obstacle squares are already visited (len(visited) == empty_cnt) and (curr_i, curr_j) == destination
constraints on next_candidates: can go to 4 neighbors
arguments pass into backtrack function: curr_i, curr_j
"""
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def backtrack(curr_i, curr_j):
            if len(visited) == empty_cnt:
                if (curr_i, curr_j) == dest:
                    self.res += 1
                return
            
            for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] != -1:  # 注意不能用==self.empty
                    if (next_i, next_j) not in visited:
                        visited.add((next_i, next_j))
                        backtrack(next_i, next_j)
                        visited.remove((next_i, next_j))
        
        
        m, n = len(grid), len(grid[0])
        start, dest = (0, 0), (0, 0)
        empty_cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    empty_cnt += 1
                elif grid[i][j] == 2:
                    dest = (i, j)
                    empty_cnt += 1
                elif grid[i][j] == 0:
                    empty_cnt += 1
                    
        self.res = 0
        visited = set()
        visited.add(start)
        backtrack(start[0], start[1])
        return self.res








"""
Solution 2: since we don't need to print the actual paths, DP or dfs with memorization is good.
Total ime complexity for this DP = No. of sub-problems * Time taken per sub-problem = O(n * 2^n) * O(1) = O(n * 2^n).
"""
import collections
class Solution:
    def uniquePathsIII(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        start, end = (0, 0), (0, 0)
        steps_needed = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 2:
                    end = (i, j)
                if grid[i][j] != -1:
                    steps_needed += 1

        visited = set()
        visited.add(start)
        
        # key is how many steps to reach (i, j), val is how many ways to use so many ways to reach(i, j)
        memo = collections.defaultdict(int)
        
        def dfs(curr_i, curr_j, steps):
            if (curr_i, curr_j, steps) in memo:
                return memo[curr_i][curr_j][steps]
            
            if (curr_i, curr_j) == end:
                return 1 if steps == steps_needed - 1 else 0
            
            ways = 0
            for delta_i, delta_j in moves:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                
                if 0 <= next_i < m and 0 <= next_j < n and \
                grid[next_i][next_j] != -1 and (next_i, next_j) not in visited:
                    visited.add((next_i, next_j))
                    ways += dfs(next_i, next_j, steps + 1)
                    visited.remove((next_i, next_j))        # backtrack
                               
            memo[(curr_i, curr_j, steps + 1)] = ways      # 注意事项steps + 1
            
            return ways
                    
        return dfs(start[0], start[1], 0)




"""
The problem stated that we need to land on each empty square exactly once, 
this simply meant the length of our unique path must equal the total number of empty squares in the grid (including start and end squares). 
After that, it's just a typical backtracking path finding problem.
solution 1: dfs+backtrack: 这种方法不但可以找出有多少种路径，而且可以打印出所有路径
O(4^N) time where N is number of non-block squares in the grid. 
"""
import collections
class Solution:
    def uniquePathsIII(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        start, end = (0, 0), (0, 0)
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 2:
                    end = (i, j)
                if grid[i][j] != -1:
                    cnt += 1

        res = []
        visited = set()
        visited.add(start)
        self.backtrack(grid, start, end, visited, cnt, [start], res)

        return len(res)     # return res 就可以打印出路径了

    def backtrack(self, grid, curr_pos, end, visited, cnt, curr_path, res):
        if curr_pos == end and len(visited) == cnt:
            res.append(curr_path.copy())        # 偶的天，总是忘了copy呀
            return

        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for delta_x, delta_y in moves:
            next_pos = (curr_pos[0] + delta_x, curr_pos[1] + delta_y)
            if 0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0]):
                if grid[next_pos[0]][next_pos[1]] != -1:
                    if next_pos not in visited:
                        visited.add(next_pos)
                        curr_path.append(next_pos)
                        self.backtrack(grid, next_pos, end, visited, cnt, curr_path, res)
                        curr_path.pop()
                        visited.remove(next_pos)
