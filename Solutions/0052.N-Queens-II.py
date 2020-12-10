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

"""
排列问题：先打印出数组[0, 1, 2, 3....n]中所有的可能排列：[[0,1,2,3], [1,3,0,2].....]，其中的每一个子数组表示一种可能的方法，
子数组中的数字表示在哪个数字的地方放一个Queen，数字对应的下标位置是放那个Queen的行，数字的值是放那个Queen的列。

由于Queen可以很冲直撞，所以列是不能相同的，所以需要去重，用visited标记就可以。
又由于Queen还可以斜着走，所以横纵坐标的和与差不能相同，也需要用visited标记。
用一个visited数组存储 列号，横纵坐标之和，横纵坐标之差 有没有被用过
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(curr_comb):
            if len(curr_comb) == n:
                res.append(curr_comb.copy())
                return
            
            for i in range(n):
                row, col = len(curr_comb), i
                
                if col in col_visited:
                    continue
                if row - col in dia_visited:
                    continue
                if row + col in adia_visited:
                    continue
                    
                curr_comb.append(col)
                col_visited.add(col)
                dia_visited.add(row - col)
                adia_visited.add(row + col)
                
                backtrack(curr_comb)
                
                curr_comb.pop()
                col_visited.remove(col)
                dia_visited.remove(row - col)
                adia_visited.remove(row + col)
        
        
        res = []
        col_visited = set()
        dia_visited = set()
        adia_visited = set()
        backtrack([])
        return len(res)







class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(curr_row, curr_col, curr_comb):
            if len(curr_comb) == n:
                res.append(curr_comb.copy())
                return
            for next_row in range(curr_row + 1, n):         # 注意不能回头找, 必须从curr_row+1开始, 
                if next_row in row_visited:   # 因为permutation[(0, 1), (1, 3), (2, 0), (3, 2)]和[(0, 1), (2, 0), (1, 3), (3, 2)]是重复的答案
                    continue
                for next_col in range(curr_col + 1, n):
                    if next_col in col_visited:
                        continue
                    if next_row + next_col in sum_visited:
                        continue
                    if next_row - next_col in diff_visited:
                        continue
                    row_visited.add(next_row)
                    col_visited.add(next_col)
                    sum_visited.add((next_row + next_col))
                    diff_visited.add((next_row - next_col))
                    curr_comb.append((next_row, next_col))
                    backtrack(next_row, curr_col, curr_comb)
                    curr_comb.pop()
                    row_visited.remove(next_row)
                    col_visited.remove(next_col)
                    sum_visited.remove((next_row + next_col))
                    diff_visited.remove((next_row - next_col))
                    
        res = []
        row_visited = set()
        col_visited = set()
        sum_visited = set()
        diff_visited = set()
        backtrack(-1, -1, [])
        return len(res)

