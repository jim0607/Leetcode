"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
"""


# dp[i][j] = the number of discinct subeseq until ith char in s and jth char in t
# if s[i]!=t[j], dp[i][j] = dp[i - 1][j]  eg: rab, ra
# else: rabb, rab, dp[i][j] = dp[i-1][j] + dp[i-1][j-1], 品，细品！
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n: return 0
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:    
                    dp[i][j] += dp[i-1][j-1]    # eg: rabb, rab
        return dp[m][n] 
