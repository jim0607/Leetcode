#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (54.84%)
# Likes:    375
# Dislikes: 132
# Total Accepted:    116.9K
# Total Submissions: 212.5K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
# 
# Example:
# 
# 
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown
# below.
# [
# [".Q..",  // Solution 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // Solution 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
#

class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        visited_col = {i: False for i in range(n)}
        visited_sum = {i: False for i in range(2 * n - 1)}
        visited_diff = {i: False for i in range(1 - n, n)}
        self.dfs(n, [], res, visited_col, visited_sum, visited_diff)
        
        return len(res)
    
    def dfs(self, n, curr, res, visited_col, visited_sum, visited_diff):
        if len(curr) == n:
            res.append(curr.copy)
            
        for i in range(n):
            row, col = len(curr), i     #准备把col放到len(curr)的位置，还没放，所以row=len(curr)而不是len(curr)-1
            if visited_col[col] or visited_sum[row + col] or visited_diff[row - col]:
                continue
            
            curr.append(col)
            visited_col[col] = True
            visited_sum[row + col] = True
            visited_diff[row - col] = True
            
            self.dfs(n, curr, res, visited_col, visited_sum, visited_diff)
            
            curr.pop()
            visited_col[col] = False
            visited_sum[row + col] = False
            visited_diff[row - col] = False
