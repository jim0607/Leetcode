"""
1293. Shortest Path in a Grid with Obstacles Elimination

Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. 
If it is not possible to find such walk return -1.

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 
Example 2:

Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
 
Constraints:

grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0
"""



"""
O(mnk), 这是因为一共可能visit m* n个点，一个点最多可能被visit k次
"""
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = defaultdict(int)  # pos --> elimination left
        q.append((0, 0, k))
        visited[(0, 0)] = k
        
        step = -1
        while len(q) > 0:
            step += 1
            lens = len(q)
            for _ in range(lens):
                curr_i, curr_j, curr_left = q.popleft()
                if (curr_i, curr_j) == (m - 1, n - 1):
                    return step
                    
                for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < m and 0 <= next_j < n:
                        if grid[next_i][next_j] == 0:
                            if (next_i, next_j) not in visited or visited[(next_i, next_j)] < curr_left:    # if we can get to (next_i, next_j) with less elimination, we should also visit
                                visited[(next_i, next_j)] = curr_left
                                q.append((next_i, next_j, curr_left))
                        else:
                            if curr_left == 0:      # if not enimilation left, we cannot pass this "1"
                                continue
                            if (next_i, next_j) not in visited or visited[(next_i, next_j)] < curr_left - 1:
                                visited[(next_i, next_j)] = curr_left - 1
                                q.append((next_i, next_j, curr_left - 1))
                                
        return -1




class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        elimination_cnt = 0
        q.append((0, 0, elimination_cnt))
        visited.add((0, 0, elimination_cnt))
        step = -1
        while len(q) > 0:
            step += 1
            lens = len(q)
            for _ in range(lens):
                curr_i, curr_j, curr_elimination_cnt = q.popleft()
                if (curr_i, curr_j) == (m - 1, n - 1):
                    return step
                for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < m and 0 <= next_j < n:
                        if grid[next_i][next_j] == 0:
                            if (next_i, next_j, curr_elimination_cnt) not in visited:
                                q.append((next_i, next_j, curr_elimination_cnt))
                                visited.add((next_i, next_j, curr_elimination_cnt))
                        elif grid[next_i][next_j] == 1:
                            if curr_elimination_cnt >= k:
                                continue
                            if (next_i, next_j, curr_elimination_cnt + 1) not in visited:
                                q.append((next_i, next_j, curr_elimination_cnt + 1))
                                visited.add((next_i, next_j, curr_elimination_cnt + 1))
        return -1
