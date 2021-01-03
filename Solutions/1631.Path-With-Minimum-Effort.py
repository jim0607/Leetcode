"""
1631. Path With Minimum Effort

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, 
where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), 
and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, 
and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:

Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 
Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
"""

"""
hq stores the (curr_maxdiff to curr_pos, curr_pos)
"""
class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        hq = [(0, 0, 0)]
        min_maxcosts = defaultdict(int)    # curr_pos --> curr_min_maxcost until curr_pos
        while len(hq) > 0:
            curr_maxcost, curr_i, curr_j = heappop(hq)
            if (curr_i, curr_j) == (m - 1, n - 1):
                return curr_maxcost
            
            if (curr_i, curr_j) in min_maxcosts:
                continue
            min_maxcosts[(curr_i, curr_j)] = curr_maxcost
            
            for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    next_maxcost = max(curr_maxcost, abs(grid[next_i][next_j] - grid[curr_i][curr_j]))
                    heappush(hq, (next_maxcost, next_i, next_j))


"""
Obviously, it is a minimum of max_val problem, which is typical Dijkstra's.
maintain a heapq to store (the max_diff in the path so far till the curr_pos, curr_pos). 
Each time, we push (max(next_diff, curr_max_diff), next_pos).
注意需要一个visited set to store the pos we visited.
"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        
        hq = [(0, 0, 0)]
        min_maxdiffs = defaultdict(int)     # curr_pos --> min_maxdiff
        
        while len(hq) > 0:
            curr_maxdiff, curr_i, curr_j = heappop(hq)
            if (curr_i, curr_j) == (m - 1, n - 1):
                return curr_maxdiff
            
            if (curr_i, curr_j) in min_maxdiffs:
                continue
            min_maxdiffs[(curr_i, curr_j)] = curr_maxdiff
            
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = curr_i + delta_i, curr_j + delta_j
                if 0 <= next_i < m and 0 <= next_j < n:
                    next_maxdiff = max(curr_maxdiff, abs(heights[next_i][next_j] - heights[curr_i][curr_j]))
                    heappush(hq, (next_maxdiff, next_i, next_j))                    
