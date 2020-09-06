#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (42.83%)
# Likes:    1353
# Dislikes: 61
# Total Accepted:    172.9K
# Total Submissions: 401.7K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# 
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
# 
# Example:
# 
# 
# Input: 4
# Output: [
# ⁠[".Q..",  // Solution 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // Solution 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above.
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
        
        # ans = []
        # for lst in res:
        #     for i, j in lst:
        #         temp_ans = [["." for _ in range(n)] for _ in range(n)]
        #         temp_ans[i][j] = "Q"
        #     ans.append(temp_ans)
        # return ans




"""
下面是优化一点的解
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.visited_col = set()
        self.visited_sum = set()
        self.visited_diff = set()
        
        self.backtrack(n, [])
        
        return self.draw(self.res)
    
    def backtrack(self, n, curr):
        if len(curr) == n:
            self.res.append(curr.copy())
            return
        
        for i in range(n):
            row, col = len(curr), i
            
            if col in self.visited_col or row+col in self.visited_sum or row-col in self.visited_diff:
                continue
                
            curr.append(col)
            self.visited_col.add(col)
            self.visited_sum.add(row+col)
            self.visited_diff.add(row-col)
            
            self.backtrack(n, curr)
            
            curr.pop()
            self.visited_col.remove(col)
            self.visited_sum.remove(row+col)
            self.visited_diff.remove(row-col)
    
    def draw(self, grid):
        results = []
        for nums in grid:
            result = []
            for col in nums:
                result.append("." * col + "Q" + "." * (len(nums) - col - 1))    
            results.append(result)
            
        return results
