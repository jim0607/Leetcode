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


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self._backtrack(n, 0, 0, "")
        return self.res
    
    def _backtrack(self, n, left_cnt, right_cnt, curr_comb):
        if left_cnt == right_cnt == n:
            self.res.append(curr_comb)  # string doesn't need deep copy because it is immutable
            return
        
        if left_cnt < right_cnt:        # 这个判断尤为关键 - strong pruning
            return
        
        if left_cnt < n:
            self._backtrack(n, left_cnt + 1, right_cnt, curr_comb + "(")
        if right_cnt < n:
            self._backtrack(n, left_cnt, right_cnt + 1, curr_comb + ")")
