"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


"""
backtrack结束条件: left_cnt == right_cnt == n
constraints on next_candidates: can only be left_parentheses or right_parentheses, left_cnt cannot exceed right_cnt
arguments pass into backtrack function: left_cnt, right_cnt, curr_comb
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left_cnt, right_cnt, curr_comb):
            if left_cnt == right_cnt == n:  
                res.append(curr_comb)   # string doesn't need deep copy because it is immutable
                return
            
            if right_cnt > left_cnt:    # 这个判断尤为关键 - strong pruning
                return
            
            if left_cnt < n:
                backtrack(left_cnt + 1, right_cnt, curr_comb + "(")
            if right_cnt < n:
                backtrack(left_cnt, right_cnt + 1, curr_comb + ")")
                
            
        res = []
        backtrack(0, 0, "")
        return res
