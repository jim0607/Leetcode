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
                self._backtrack(S, next_idx, curr_str + S[next_idx], res)
            else:
                self._backtrack(S, next_idx, curr_str + S[next_idx].upper(), res)
                self._backtrack(S, next_idx, curr_str + S[next_idx].lower(), res)
