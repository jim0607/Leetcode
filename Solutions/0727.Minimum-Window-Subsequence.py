"""
727. Minimum Window Subsequence

Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
"""



"""
naive sliding window - O(MN)
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_lens = len(s)
        res = ""
        j = 0
        for i in range(len(s)):     # O(N)
            while j < len(s) and not self._is_subseq(s[i:j], t):
                j += 1
            
            if j - i < min_lens and self._is_subseq(s[i:j], t):
                min_lens = j - i
                res = s[i:j]        # O(N) here could be optimized to O(1), see below solution
        
        return res
    
    def _is_subseq(self, s, t):       # taks O(M)
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(t)
        
        
        
"""
a little faster liding window - still O(MN)
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_lens = len(s)
        j = 0
        start, end = 0, 0
        for i in range(len(s)):
            while j < len(s) and not self._is_subseq(s, i, j, t):
                j += 1
            
            if j - i < min_lens and self._is_subseq(s, i, j, t):
                min_lens = j - i
                start, end = i, j
        
        return s[start:end]
    
    def _is_subseq(self, s, start, end, t):
        i, j = start, 0
        while i < end and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(t)
        
        
"""
solution 3: dp
dp[i][j] = the min window subsequence that ends with ith ch in t, and jth ch in s.
If t[i-1] == s[j-1]: dp[i][j] = dp[i-1][j-1] + 1; else: dp[i][j] = dp[i][j-1] + 1
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(t), len(s)
        dp = [[20000 for _ in range(n + 1)] for _ in range(m + 1)]  # 20000是因为题目给的len(s)<20000
        for j in range(n + 1):
            dp[0][j] = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1] + 1
        
        min_len = min(dp[-1])
        if min_len == 20000: return ""
        for j in range(1, n + 1):
            if dp[-1][j] == min_len:
                return s[j-min_len:j]
