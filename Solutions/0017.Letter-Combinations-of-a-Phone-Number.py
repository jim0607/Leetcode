"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""


"""
套用backtrack的模板，这里的next_idx只能取curr_idx + 1, 因为我们要在s里一个一个往前
"""
"""
backtrack结束条件：if len(curr_comb) == len(digits).
next_ch的constraint: must be in mapping[digits[curr_dix+1]].
pass into backtrack: curr_idx, curr_comb
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']}
        
        
        def backtrack(curr_idx, curr_comb):
            if len(curr_comb) == len(digits):
                res.append(curr_comb)
                return
            
            for next_ch in mapping[digits[curr_idx + 1]]:   # 这里的next_idx只能取curr_idx + 1, 因为我们要在s里一个一个往前
                backtrack(curr_idx + 1, curr_comb + next_ch)
                
                
        if len(digits) == 0:
            return []
        
        res = []
        backtrack(-1, "")
        return res


    
    
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        self.phone = {
         '2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}
        
        self.res = []
        self.backtrack(digits, 0, [])
        
        return self.res
    
    def backtrack(self, digits, currIdx, curr):
        if currIdx == len(digits):
            self.res.append("".join(curr))  # string is immutable so don't need deep copy
            return
        
        for ch in self.phone[digits[currIdx]]:
            curr.append(ch)
            self.backtrack(digits, currIdx + 1, curr)
            curr.pop()
