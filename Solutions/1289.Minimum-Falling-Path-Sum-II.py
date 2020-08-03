1289. Minimum Falling Path Sum II

Given a square grid of integers arr, a falling path with non-zero shifts is a choice of exactly one element from each row of arr, such that no two elements chosen in adjacent rows are in the same column.

Return the minimum sum of a falling path with non-zero shifts.

 

Example 1:

Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.



"""
solution 1: 我们可以每次都去找上一行中除去j的最小值 - O(MN^2).
solution 2: 将上一行的fisrt_min和second_min提前计算好 - O(MN) similar with 265. Paint House II
"""
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        m, n = len(arr), len(arr[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[0][j] = arr[0][j]
        
        for i in range(1, m):
            
            # step 1: pre-calculate the min_1, min_2, min_idx_1, min_idx_2
            min_1, min_2 = float("inf"), float("inf")
            min_idx_1, min_idx_2 = -1, -1
            for j in range(n):
                if dp[i-1][j] < min_1:
                    min_1, min_2 = dp[i-1][j], min_1
                    min_idx_1, min_idx_2 = j, min_idx_1
                elif min_1 <= dp[i-1][j] < min_2:
                    min_2 = dp[i-1][j]
                    min_idx_2 = j
                    
            # step 2: update dp[i] using the pre-calculated min_1, min_2
            for j in range(n):
                if j == min_idx_1:
                    dp[i][j] = min_2 + arr[i][j]
                else:
                    dp[i][j] = min_1 + arr[i][j]
                    
        return min(dp[m-1][j] for j in range(n))
