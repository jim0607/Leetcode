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


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.backtrack(n, 0, 0, "")
        
        return self.res
    
    def backtrack(self, n, leftCnt, rightCnt, curr):
        if leftCnt == n and rightCnt == n:
            self.res.append(curr)
            return
        
        if leftCnt < rightCnt:  # 这个判断尤为关键！
            return
        
        if leftCnt < n:
            self.backtrack(n, leftCnt + 1, rightCnt, curr + "(")
            
        if rightCnt < n:
            self.backtrack(n, leftCnt, rightCnt + 1, curr + ")")
