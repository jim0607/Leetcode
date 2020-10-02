"""
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


"""
每一个转弯的点是dfs的node, dfs helper function 需要传入的参数有(当前的位置, 当前的方向，当前的row_range and col_range)
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def dfs(curr_i, curr_j, curr_dir, min_row, max_row, min_col, max_col):
            if len(res) == m * n:
                return
            if curr_dir == "r":
                for j in range(min_col, max_col + 1):
                    res.append(matrix[curr_i][j])
                dfs(curr_i, j, "d", min_row + 1, max_row, min_col, max_col)
            elif curr_dir == "d":
                for i in range(min_row, max_row + 1):
                    res.append(matrix[i][curr_j])
                dfs(i, curr_j, "l", min_row, max_row, min_col, max_col - 1)
            elif curr_dir == "l":
                for j in range(max_col, min_col - 1, -1):
                    res.append(matrix[curr_i][j])
                dfs(curr_i, j, "u", min_row, max_row - 1, min_col, max_col)
            elif curr_dir == "u":
                for i in range(max_row, min_row - 1, -1):
                    res.append(matrix[i][curr_j])
                dfs(i, curr_j, "r", min_row, max_row, min_col + 1, max_col)        
        
        
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        dfs(0, 0, "r", 0, m - 1, 0, n - 1)
        return res
