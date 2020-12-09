"""
1368. Minimum Cost to Make at Least One Valid Path in a Grid

Given a m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some invalid signs on the cells of the grid which points outside the grid.

You will initially start at the upper left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) 
and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path doesn't have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

Example 1:

Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) 
change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) 
change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.
Example 2:

Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).
Example 3:

Input: grid = [[1,2],[4,3]]
Output: 1
Example 4:

Input: grid = [[2,2,2],[2,2,2]]
Output: 3
Example 5:

Input: grid = [[4]]
Output: 0
"""


"""
由于我们可以选择四个方向都可以走，所以不能用dp. 如果只能朝右下方向走才能用dp.
可以朝四个方向走只能用bfs/dfs.
由于我们需要maitain min_cost, 所以可以用Dijkstra's.
heapq stores (curr_cost, curr_i, curr_j). 
O(NlogN), where N is the number of cells in grid.
"""
"""
heapq stores (curr_cost, curr_pos)
costs dictionary maps (curr_pos --> min cost to reach the curr_pos)
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        mapping = {3: (1, 0), 4: (-1, 0), 1: (0, 1), 2: (0, -1)}
        
        hq = [(0, 0, 0)]
        costs = defaultdict(int)
        
        while len(hq) > 0:
            curr_cost, curr_i, curr_j = heappop(hq)
            
            if (curr_i, curr_j) == (m - 1, n - 1):
                return curr_cost
            
            if (curr_i, curr_j) in costs:
                continue
            costs[(curr_i, curr_j)] = curr_cost
            
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    next_cost = 0 if mapping[grid[curr_i][curr_j]] == (delta_i, delta_j) else 1
                    heappush(hq, (curr_cost + next_cost, next_i, next_j))
