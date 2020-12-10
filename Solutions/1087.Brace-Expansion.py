"""
1087. Brace Expansion

A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  
If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.

Example 1:

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: "abcd"
Output: ["abcd"]
"""


"""
套用dfs模板即可 - O(M^N), where N is len(lst), M is avg how many choices we have for each string in lst.
"""
class Solution:
    def expand(self, s: str) -> List[str]:
        def backtrack(curr_idx, curr_comb):
            if len(curr_comb) == len(chs):
                res.append(curr_comb)
                return
            for ch in lst[curr_idx + 1]:        # next_idx 只能等于curr_idx + 1
                backtrack(curr_idx + 1, curr_comb + ch)
        
        
        lst = self._construct_lst(s)    # "{a,b}b{d,e}f" --> ['ab', 'b', 'de', 'f']
        res = []
        backtrack(-1, "")
        return sorted(res)
        
        
    def _construct_lst(self, s):
        lst = []
        i = 0
        while i < len(s):
            if s[i] == "{":
                j = i
                temp = ""
                while j < len(s) and s[j] != "}":
                    j += 1
                    if s[j].isalpha():
                        temp += s[j]
                lst.append(temp)
                i = j + 1
            elif s[i].isalpha():
                lst.append(s[i])
                i += 1
        return lst
