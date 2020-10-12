"""
1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

Given a m x n matrix mat and an integer threshold. 
Return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

Example 1:

Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
Example 3:

Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
Output: 3
Example 4:

Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output: 2

1 <= m, n <= 300
m == mat.length
n == mat[i].length
0 <= mat[i][j] <= 10000
0 <= threshold <= 10^5
"""



"""
solution 1: max problem - binary search O(mnlogmn)
"""
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # step 1: construct the 2D pre_sum - 注意要用两个for loop来construct pre_sum
        m, n = len(mat), len(mat[0])
        pre_sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):  
            for j in range(n):
                pre_sum[i+1][j+1] = pre_sum[i+1][j] + mat[i][j]
        for j in range(n):
            for i in range(m):
                pre_sum[i+1][j+1] += pre_sum[i][j+1]
                
        # step 2: binary search for the max_square_lens
        start, end = 0, min(m, n)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._is_valid(pre_sum, threshold, mid):
                start = mid
            else:
                end = mid
        return end if self._is_valid(pre_sum, threshold, end) else start
    
    def _is_valid(self, pre_sum, threshold, L):
        """
        Return whether or not there is a L-size square block in mat that sum up <= threshold
        """
        m, n = len(pre_sum) - 1, len(pre_sum[0]) - 1
        
        # fix左上角的点来遍历matrix
        for i in range(m):
            for j in range(n):
                if i + L <= m and j + L <= n:
                    block_sum = pre_sum[i+L][j+L] - pre_sum[i+L][j] - pre_sum[i][j+L] + pre_sum[i][j]
                    if block_sum <= threshold:
                        return True
        return False
        
        
"""
solution 2: prefix sum. Think about 1D problem: Maximum subarray Sum Less than K.
Then it is a typical sliding window window problem.
O(mn)
"""
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # step 1: construct the 2D pre_sum - 注意要用两个for loop来construct pre_sum
        m, n = len(mat), len(mat[0])
        pre_sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):  
            for j in range(n):
                pre_sum[i+1][j+1] = pre_sum[i+1][j] + mat[i][j]
        for j in range(n):
            for i in range(m):
                pre_sum[i+1][j+1] += pre_sum[i][j+1]
                
        # step 2: sliding window to find Maximum subarray Sum Less than K
        max_len = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                next_len = max_len + 1
                if i >= next_len and j >= next_len and pre_sum[i][j] - pre_sum[i-next_len][j] - pre_sum[i][j-next_len] + pre_sum[i-next_len][j-next_len] <= threshold:
                    max_len = next_len
        return max_len
