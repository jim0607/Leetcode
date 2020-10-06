"""
463. Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, 
and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
"""



class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # step 1: find the min_row, max_row, min_col, max_col for the island
        min_row, max_row = m - 1, 0
        min_col, max_col = n - 1, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)

        # step 2: update the res row by row, col by col
        res = 0
        for i in range(min_row, max_row + 1):
            for j in range(min_col, max_col + 1):
                if grid[i][j] == 1:
                    if i == min_row or grid[i-1][j] == 0:
                        res += 1
                    if i == max_row or grid[i+1][j] == 0:
                        res += 1
                    if j == min_col or grid[i][j-1] == 0:
                        res += 1
                    if j == max_col or grid[i][j+1] == 0:
                        res += 1
        return res
