"""
由于我们可以选择四个方向都可以走，所以不能用dp. 如果只能朝右下方向走才能用dp.
可以朝四个方向走只能用bfs/dfs.
由于我们需要maitain min_cost, 所以可以用Dijkstra's.
heapq stores (curr_cost, curr_i, curr_j). 
O(NlogN), where N is the number of cells in grid.
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        hq = []
        visited = set()
        heappush(hq, (0, 0, 0))
        visited.add((0, 0, 0))
        while len(hq) > 0:
            curr_cost, curr_i, curr_j = heappop(hq)
            if (curr_i, curr_j) == (m - 1, n - 1):
                return curr_cost
            
            for direction, (delta_i, delta_j) in directions.items():
                if grid[curr_i][curr_j] == direction:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < m and 0 <= next_j < n:
                        if (curr_cost, next_i, next_j) not in visited:
                            heappush(hq, (curr_cost, next_i, next_j))
                            visited.add((curr_cost, next_i, next_j))
                else:
                    next_i, next_j = curr_i + delta_i, curr_j + delta_j
                    if 0 <= next_i < m and 0 <= next_j < n:
                        if (curr_cost + 1, next_i, next_j) not in visited:
                            heappush(hq, (curr_cost + 1, next_i, next_j))
                            visited.add((curr_cost + 1, next_i, next_j))
