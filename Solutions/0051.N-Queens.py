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
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        if n == 0:
            return []

        visited_col = {i: False for i in range(n)}
        visited_sum = {i: False for i in range(2 * n - 1)}
        visited_diff = {i: False for i in range(1 - n, n)}

        # 打印出数组nums中所有的可能排列：[[0,1,2,3], [1,3,0,2].....]
        # 这里的数组nums其实就是[0, 1, 2, 3....n]，下标与数值相等。len(nums) = n, nums[i] = i
        self.dfs(n, [], visited_col, visited_sum, visited_diff, res)

        print(res)
 
        return self.draw(res)

    def dfs(self, n: int, curr: List[int], visited_col, visited_sum, visited_diff, res: List[List[int]]):
        if len(curr) == n:
            res.append(curr.copy())     # deep copy
            return
        
        for i in range(n):
            if not self.is_valid(curr, visited_col, visited_sum, visited_diff, i):
                continue
            
            curr.append(i)
            row, col = len(curr) - 1, i
            visited_col[col] = True
            visited_sum[row + col] = True
            visited_diff[row - col] = True

            self.dfs(n, curr, visited_col, visited_sum, visited_diff, res)

            curr.pop()
            visited_col[col] = False
            visited_sum[row + col] = False
            visited_diff[row - col] = False

    def is_valid(self, curr, visited_col, visited_sum, visited_diff, i):
        row, col = len(curr), i
        if visited_col[col]:
            return False
        if visited_sum[row + col]:
            return False
        if visited_diff[row - col]:
            return False

        return True

    def draw(self, res: List[List[int]]) -> List[List[str]]:
        draw_results = []       # a 2D List, List[List[str]]
        for permutation in res:
            draw_result = []
            for col in permutation:
                draw_str = ""
                for c in range(len(permutation)):
                    if c == col:
                        draw_str += "Q"
                    else:
                        draw_str += "."
                draw_result.append(draw_str)
            draw_results.append(draw_result)

        return draw_results
        
# @lc code=end

