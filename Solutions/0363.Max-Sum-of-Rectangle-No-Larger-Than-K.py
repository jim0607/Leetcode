"""
363. Max Sum of Rectangle No Larger Than K

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
"""



class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # step 1: construct the prefix sum for the matrix
        m, n = len(matrix), len(matrix[0])
        pre_sum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                pre_sum[i+1][j+1] = pre_sum[i][j+1] + pre_sum[i+1][j] - pre_sum[i][j] + matrix[i][j]
                
        # print(pre_sum)
        
        # step 2: update res - O(m*m*n*n)
        max_sum = float("-inf")
        for i in range(1, m+1):
            for j in range(1, n+1):
                for p in range(i):
                    for q in range(j):
                        sum = pre_sum[i][j] - pre_sum[i][q] - pre_sum[p][j] + pre_sum[p][q]
                        if sum <= k and sum > max_sum:
                            max_sum = sum
        return max_sum
        
        
"""
Follow up: What if the number of rows is much larger than the number of columns?
solution: use binary seach for rows to achieve O(n*n*m*logm)
"""
