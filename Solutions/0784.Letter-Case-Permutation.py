784. Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]



"""
backtrack - O(2^N)
"""
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(curr_idx, curr_comb):
            if len(curr_comb) == len(s):
                res.append("".join(curr_comb.copy()))
                return
            for next_idx in range(curr_idx + 1, len(s)):    # 注意这个题目next_idx不能往回找，
                if s[next_idx].isdigit():                   # 不然的话"a1b2"-->"1a2b"就变成valid答案了
                    curr_comb.append(s[next_idx])
                    backtrack(next_idx, curr_comb)
                    curr_comb.pop()
                elif s[next_idx].isalpha():
                    for ch in [s[next_idx].upper(), s[next_idx].lower()]:
                        curr_comb.append(ch)
                        backtrack(next_idx, curr_comb)
                        curr_comb.pop()
  
        res = []
        backtrack(-1, [])
        return res



"""
下面的写法更加简洁
"""
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self._backtrack(S, -1, "", res)
        return res
    
    def _backtrack(self, S, curr_idx, curr_str, res):
        if curr_idx == len(S) - 1 and len(curr_str) == len(S):
            res.append(curr_str)
            return
    
        for next_idx in range(curr_idx + 1, len(S)):
            if S[next_idx].isdigit():
                self._backtrack(S, next_idx, curr_str + S[next_idx], res)   # 这里不需要append和pop是因为curr_str是immutable的，不会改变所以不能改过来改过去
            else:
                self._backtrack(S, next_idx, curr_str + S[next_idx].upper(), res)
                self._backtrack(S, next_idx, curr_str + S[next_idx].lower(), res)
