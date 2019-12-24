Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true


"""think it as a long 1D array with m*n element, they are sorted, then we can use binary search
O(log(M*N))"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return False
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] >= target:
                end = mid
            else:
                start = mid
        if matrix[start//n][start%n] == target or matrix[end//n][end%n] == target:
            return True
        return False


"""locate the row first, then binary search in the row
O(N)"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return False
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                break
        start, end = 0, n - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[i][mid] >= target:
                end = mid
            else:
                start = mid
        if matrix[i][end] == target or matrix[i][start] == target:
            return True
        else:
            return False  
