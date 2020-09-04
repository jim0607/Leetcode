1091. Shortest Path in Binary Matrix

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

Example 1:

Input: [[0,1],[1,0]]

Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]

Output: 4

Note:
1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1




class Solution:
    MOVES = [(1, 0), (-1, 0), (1, 1), (-1, 1), (0, 1), (0, -1), (1, -1), (-1, -1)]
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        source = (0, 0)
        target = (m-1, n-1)
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        
        q = collections.deque()
        visited = set()
        q.append(source)
        visited.add(source)
        steps = 0
        while q:
            lens = len(q)
            steps += 1
            for _ in range(lens):
                curr_x, curr_y = q.popleft()
                if (curr_x, curr_y) == target:
                    return steps
                
                for delta_x, delta_y in self.MOVES:
                    next_x, next_y = curr_x + delta_x, curr_y + delta_y
                    if self.isNotValid(next_x, next_y, grid):
                        continue
                    if (next_x, next_y) in visited:
                        continue
                    q.append((next_x, next_y))
                    visited.add((next_x, next_y))
       
        return -1
    
    def isNotValid(self, x, y, grid):
        m, n = len(grid), len(grid[0])
        if x < 0 or x >= m or y < 0 or y >= n:
            return True
        if grid[x][y] == 1:
            return True
        
        return False
        
"""
bfs: O(N) where N is the number of nodes in the graph
"""    
        
        
"""
If you need to find shortest path between just two points, then A* search shows better performance than bfs.
From implementation perspective it the same code just swapping the queue with a priority queue.
On each iteration you estimate minimum path to the goal by:
f((i,j))=g((i,j))+h((i,j))
Where:
g((i,j)) = shortest path length found so far from start to (i, j)
h((i,j)) = estimation to reach goal - bottom-right cell. For cell (i, j) it is calculated simply by max(m - i - 1, n - j - 1).
Important for A* search is that h((i,j)) does not overestimate the actual cost to get to the goal.
"""
"""
A*: time complexity: 不好算，depends on the graph (how 0s and 1s are distributed)
"""
"""
A* is better than bfs in finding the shorted path from source node to end node. 这是一道经典的A* 题，很有启发性，
只要可以想到可行的heuristic estimation的方法，都可以尝试将bfs改成更快的A* . 
bfs 需要visit every node. but A* only greedily choose the best route to go. The best route is estimated by heuristic estimation.
"""
class Solution:
    EMPTY = 0
    BLOCK = 1
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        
        destination = (m-1, n-1)
        
        # (1. curr_heuristic_estimation of min # of steps from source to target if 经过currNode; 2. curr_steps from source to curr_node; 3. curr_pos))
        # curr_heuristic_estimation = curr_steps + heuristic estimation of minimum distance from curr_pos to desitination.
        hq = [(max(m, n), 1, (0, 0))]   
        steps = collections.defaultdict(int)   # position --> steps from source to curr_node. 用一个dictionary记录curr_steps是很有必要的!!
        
        while len(hq) > 0:
            curr_heuristic_estimation, curr_steps, (curr_i, curr_j)  = heappop(hq)
            if (curr_i, curr_j) == destination:
                return curr_steps
            
            for delta_i, delta_j in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == self.EMPTY:
                    
                    # 这一句是精华，如果之前访问过(next_x, next_y)，但是这次访问的时候发现能更快到达，
                    # 那就把这个(next_x, next_y)重新再次放进去, 这就是为什么需要用一个dictionary记录curr_steps
                    if (next_i, next_j) not in steps or curr_steps + 1 < steps[(next_i, next_j)]:
                        steps[(next_i, next_j)] = curr_steps + 1        # 更新从source到(next_x, next_y)的距离
                        next_heuristic_estimation = curr_steps + 1 + max(m - next_i, n - next_j)    
                        heappush(hq, (next_heuristic_estimation, curr_steps + 1, (next_i, next_j)))
        return -1
"""
想想这个题的执行顺序for this example: [[0,1,0,1,0],[1,0,0,0,1],[0,0,1,1,1],[0,0,0,0,0],[1,0,1,0,0]]
还真和wiki上的动画执行顺序一模一样
https://en.wikipedia.org/wiki/A*_search_algorithm
"""



""""
下面这种带层序遍历的A*是行不通的，steps必须进heapq里面。Same for Dijkstra's
"""
from heapq import *
class Solution:
    MOVES = [(1, 0), (-1, 0), (1, 1), (-1, 1), (0, 1), (0, -1), (1, -1), (-1, -1)]
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        source = (0, 0)
        target = (m-1, n-1)
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        
        hq = []
        visited = set()
        heappush(hq, (max(m, n), source))  # max(m, n) is a heuristic ⁄hjuˈrɪstɪk⁄ estimate of the distance of current node to target, not accurate, but works
        visited.add(source)
        dist = 0
        while hq:
            dist += 1   # distance to the source
            (curr_x, curr_y) = heappop(hq)[1]
            print((curr_x, curr_y))
            if (curr_x, curr_y) == target:
                return dist

            for delta_x, delta_y in self.MOVES:
                next_x, next_y = curr_x + delta_x, curr_y + delta_y
                if self.isNotValid(next_x, next_y, grid):
                    continue
                if (next_x, next_y) in visited:
                    continue
                heapq.heappush(hq, (max(m - next_x, n - next_y), (next_x, next_y)))
                visited.add((next_x, next_y))
       
        return -1
    
    def isNotValid(self, x, y, grid):
        m, n = len(grid), len(grid[0])
        if x < 0 or x >= m or y < 0 or y >= n:
            return True
        if grid[x][y] == 1:
            return True
        
        return False
