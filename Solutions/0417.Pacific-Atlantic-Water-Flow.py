417. Pacific Atlantic Water Flow

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).



"""
题目的意思是外围一圈的地方是water进来的地方，左上角的外围是pacific ocean water进来的地方，右下角的外围是atlantic ocean water进来的地方。
step 1: 从左上角外围的每个点出发做dfs, next_pos is a valid candidate if matrix[curr_pos] <= matrix[next_pos], 
如果能visited就存起来表示pacific ocean water可以到达这个pos；
step 2: 同样的方法记录atlantic ocean water可以达到的pos.  然后用2nd pass 来找到哪些点是两个ocean都能到达的。
"""
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        p_visited = set()
        a_visited = set()
            
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def dfs(curr_i, curr_j, visited):
            for delta_i, delta_j in moves:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and (next_i, next_j) not in visited \
                and matrix[curr_i][curr_j] <= matrix[next_i][next_j]:
                    visited.add((next_i, next_j))
                    dfs(next_i, next_j, visited)

        for i in range(m):
            p_visited.add((i, 0))
            dfs(i, 0, p_visited)       # 从左边外围出发做dfs标记pacific ocean water能到的地方
            a_visited.add((i, n -1))
            dfs(i, n - 1, a_visited)   # 从右边外围出发做dfs标记atlantic ocean water能到的地方
            
        for j in range(n):
            p_visited.add((0, j))
            dfs(0, j, p_visited)
            a_visited.add((m - 1, j))
            dfs(m - 1, j, a_visited)
                    
                    
        # 用2nd pass 来找到哪些点是两个ocean都能到达的
        res = []
        for i, j in p_visited:
            if (i, j) in a_visited:
                res.append([i, j])
                
        return res
        
        
        
"""
same idea, bfs can also make it
"""
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        p_q = collections.deque()
        p_visited = set()
        a_q = collections.deque()
        a_visited = set()
            
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def bfs(q, visited):
            while q:
                curr_i, curr_j = q.popleft()
                for delta_i, delta_j in moves:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < m and 0 <= next_j < n and (next_i, next_j) not in visited \
                    and matrix[curr_i][curr_j] <= matrix[next_i][next_j]:
                        q.append((next_i, next_j))
                        visited.add((next_i, next_j))

        for i in range(m):
            p_q.append((i, 0))
            p_visited.add((i, 0))
            bfs(p_q, p_visited)       # 从左边外围出发做dfs标记pacific ocean water能到的地方
            
            a_q.append((i, n - 1))
            a_visited.add((i, n -1))
            bfs(a_q, a_visited)   # 从右边外围出发做dfs标记atlantic ocean water能到的地方
            
        for j in range(n):
            p_q.append((0, j))
            p_visited.add((0, j))
            bfs(p_q, p_visited)
            
            a_q.append((m - 1, j))
            a_visited.add((m - 1, j))
            bfs(a_q, a_visited)        
                    
        # 用2nd pass 来找到哪些点是两个ocean都能到达的
        res = []
        for i, j in p_visited:
            if (i, j) in a_visited:
                res.append([i, j])
                
        return res
