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
"""
O(5^(n//2))
"""
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def backtrack(curr_comb):
            if len(curr_comb) == n // 2:
                res.append(curr_comb)
                return
            
            for next_num in mapping:
                if len(curr_comb) == 0 and next_num == "0":     # avoid the leading 0
                    continue
                backtrack(curr_comb + next_num)
        
        
        mapping = {"6": "9", "9": "6", "1": "1", "0": "0", "8": "8"}
        same = {"1": "1", "0": "0", "8": "8"}
        res = []
        backtrack("")
        
        ans = []
        if n % 2 == 0:
            for left in res:
                right = "".join([mapping[left[i]] for i in range(len(left) - 1, -1, -1)])
                ans.append(left + right)
        elif n % 2 == 1:
            for left in res:
                right = "".join([mapping[left[i]] for i in range(len(left) - 1, -1, -1)])
                for ch in same:
                    ans.append(left + ch + right)        
        return ans
    
    
    
"""
O(5^(n))
"""
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def backtrack(curr_comb):
            if len(curr_comb) == n:
                if is_strobogrammatic(curr_comb):
                    res.append(curr_comb)
                return
            
            for next_num in mapping:
                if len(curr_comb) == 0 and next_num == "0":
                    continue
                backtrack(curr_comb + next_num)
                
                
        def is_strobogrammatic(s):
            i, j = 0, len(s) - 1
            while i <= j:       # 注意这里要 <=
                if s[i] not in mapping or s[j] not in mapping:
                    return False
                if mapping[s[i]] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        
        mapping = {"6": "9", "9": "6", "1": "1", "0": "0", "8": "8"}
        res = []
        backtrack("")
        if n == 1:
            res.append("0")
        return res
