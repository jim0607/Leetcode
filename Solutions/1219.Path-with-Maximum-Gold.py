1219. Path with Maximum Gold

In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.


"""
尝试每一个pos出发backtrack最多能得到的gold - O((MN)^2).
没经过一个点就把这个地方的矿标记为0, 以后不能再访问了
"""
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    # 后面的dfs会修改grid的值，所以用temp, 注意必须要这样copy下来grid, 不然后面temp改变的话grid还是会跟着变
                    temp = [[grid[i][j] for j in range(n)] for i in range(m)]       
                    temp[i][j] = 0      # 标记为0, 相当于标记visited
                    self._backtrack(temp, i, j, grid[i][j])

        return self.max_gold
    
    def _backtrack(self, grid, curr_i, curr_j, curr_sum):
        self.max_gold = max(self.max_gold, curr_sum)
        for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_i, next_j = curr_i + delta_i, curr_j + delta_j
            if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]):
                if grid[next_i][next_j] != 0:
                    next_gold = grid[next_i][next_j]
                    grid[next_i][next_j] = 0        # 标记为0, 相当于标记visited
                    self._backtrack(grid, next_i, next_j, curr_sum + next_gold)
                    grid[next_i][next_j] = next_gold        # backtrack回去
