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



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        self.next_dir = {"right": "down", "down": "left", "left": "up", "up": "right"}
        self._helper(matrix, 0, 0, [0, m - 1], [0, n - 1], "right", res)
        return res
    
    def _helper(self, matrix, curr_row, curr_col, curr_row_range, curr_col_range, curr_dir, res):
        """
        需要传入的参数有，当前的位置，当前的row_range and col_range, 当前的方向
        """
        if len(res) == len(matrix) * len(matrix[0]):
            return 
        
        row_start, row_end = curr_row_range[0], curr_row_range[1]
        col_start, col_end = curr_col_range[0], curr_col_range[1]
        
        if curr_dir == "right":
            print(curr_row, col_start, col_end)
            res += matrix[curr_row][col_start:col_end + 1]
            curr_row += 1
            curr_col = col_end
            curr_dir = self.next_dir[curr_dir]
            self._helper(matrix, curr_row, curr_col, [curr_row, row_end], curr_col_range, curr_dir, res)
        
        elif curr_dir == "down":
            res += [matrix[row][curr_col] for row in range(row_start, row_end + 1)]
            curr_col -= 1
            curr_row = row_end
            curr_dir = self.next_dir[curr_dir]
            self._helper(matrix, curr_row, curr_col, curr_row_range, [col_start, curr_col], curr_dir, res)
            
        elif curr_dir == "left":
            res += matrix[curr_row][col_start:col_end + 1][::-1]
            curr_row -= 1
            curr_col = col_start
            curr_dir = self.next_dir[curr_dir]
            self._helper(matrix, curr_row, curr_col, [row_start, curr_row], curr_col_range, curr_dir, res)
        
        elif curr_dir == "up":
            res += [matrix[row][curr_col] for row in range(row_start, row_end + 1)][::-1]
            curr_col += 1
            curr_row = row_start
            curr_dir = self.next_dir[curr_dir]
            self._helper(matrix, curr_row, curr_col, curr_row_range, [curr_col, col_end], curr_dir, res)
