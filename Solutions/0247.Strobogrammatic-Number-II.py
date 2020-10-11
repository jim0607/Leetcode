"""
247. Strobogrammatic Number II

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""


"""
once the left half of the valid string s is fixed, then we can find the right half.
so we can find all combinations for n//2 lens, using backtrack.
"""
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:        
        def backtrack(curr_comb, curr_len):
            if curr_len == n // 2:
                res.append(curr_comb)
                return
            
            for next_digit in mapping:
                if curr_len == 0 and next_digit == "0":     # avoid the leading 0
                    continue
                backtrack(curr_comb + next_digit, curr_len + 1)
        
        
        mapping = {"6": "9", "9": "6", "1": "1", "0": "0", "8": "8"}
        same = {"1": "1", "0": "0", "8": "8"}
        
        res = []
        backtrack("", 0)
        
        ans = []
        if n % 2 == 0:
            for s in res:
                right_half = ""
                for j in range(len(s) - 1, -1, -1):
                    right_half += mapping[s[j]]
                ans.append(s + right_half)
        else:
            for s in res:
                for ch in same:    # 注意we can only choose ch in same as mid ch
                    right_half = ch
                    for j in range(len(s) - 1, -1, -1):
                        right_half += mapping[s[j]]
                    ans.append(s + right_half)
        return ans
