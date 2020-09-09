934. Shortest Bridge

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: A = [[0,1],[1,0]]
Output: 1
Example 2:

Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


 
"""
setp 1: 用outliners_1, outliners_2 = set(), set()找到两个island的outliner. 
step 2: 接下来是多源节点出发求最短路径问题 - bfs.
这题的关键是怎样找一个岛屿的outliners.
"""
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(curr_i, curr_j, outliners):
            visited.add((curr_i, curr_j))
            for delta_i, delta_j in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if grid[next_i][next_j] == 0:       # ****注意这样找一个连通区域的outliners - 将周围的0加入到outliners
                        outliners.add((next_i, next_j)) # 也可以outliners.add((curr_i, curr_j)) - 将最外层的1加入到outliners
                    elif grid[next_i][next_j] == 1:
                        if (next_i, next_j) not in visited:
                            dfs(next_i, next_j, outliners)
                                       
        # step 1: dfs找到两个独立岛屿的outliners
        m, n = len(grid), len(grid[0])
        visited = set()
        outliners_1, outliners_2 = set(), set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    if len(outliners_1) == 0:
                        dfs(i, j, outliners_1)
                    else:
                        dfs(i, j, outliners_2)
        
        # step 2: 接下来是多源节点出发求最短路径问题 - bfs
        q = collections.deque()
        visited = set()
        for i, j in outliners_1:
            q.append((i, j))
            visited.add((i, j))
        steps = 0
        while len(q) > 0:
            steps += 1
            lens = len(q)
            for _ in range(lens):
                curr_i, curr_j = q.popleft()
                if (curr_i, curr_j) in outliners_2:     # when reached desitination
                    return steps
                for delta_i, delta_j in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < m and 0 <= next_j < n:
                        if grid[next_i][next_j] == 0:
                            if (next_i, next_j) not in visited:
                                q.append((next_i, next_j))
                                visited.add((next_i, next_j))
        return steps
 
 
 
 

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(A), len(A[0])
        
        visited = set()
        outliners_1, outliners_2 = set(), set()
        
        def dfs(curr_i, curr_j, outliners):
            for delta_i, delta_j in moves:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if A[next_i][next_j] == 0:
                        outliners.add((curr_i, curr_j))   # 也可以outliners.add((next_i, next_j))
                    else:
                        if (next_i, next_j) not in visited:
                            visited.add((next_i, next_j))
                            dfs(next_i, next_j, outliners)
        
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    if (i, j) not in visited:
                        if not outliners_1:
                            visited.add((i, j))
                            dfs(i, j, outliners_1)
                        else:
                            visited.add((i, j))
                            dfs(i, j, outliners_2)

        # actually don't need bfs, since we can either pass 1 or 0 on the path, so we can just directly calculate the Manhatton Distance
        min_dist = float("inf")
        for i, j in outliners_1:
            for k, p in outliners_2:
                min_dist = min(abs(i - k) + abs(j - p)  - 1, min_dist)
        
        return min_dist
