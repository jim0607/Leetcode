"""
1314. Matrix Block Sum

Given a m * n matrix mat and an integer K, 
return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, 
and (r, c) is a valid position in the matrix.
 
Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 
Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
"""


"""
similar with 304. Range Sum Query 2D - Immutable
"""
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        pre_sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):  
            for j in range(n):
                pre_sum[i+1][j+1] = pre_sum[i+1][j] + mat[i][j]
        for j in range(n):
            for i in range(m):
                pre_sum[i+1][j+1] += pre_sum[i][j+1]
                
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                min_row = max(0, i - k)
                max_row = min(m - 1, i + k)
                min_col = max(0, j - k)
                max_col = min(n - 1, j + k)
                block_sum = pre_sum[max_row+1][max_col+1] - pre_sum[max_row+1][min_col] - pre_sum[min_row][max_col+1] + pre_sum[min_row][min_col]
                res[i][j] = block_sum
        return res
                          
