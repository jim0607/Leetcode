Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

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


"""f[i][j]=B前i个字符B[0..i)在A前j个字符A[0..j)中出现多少次
f[i][j] += f[i][j-1]; if B[i-1]=A[j-1] += f[i-1][j-1] + f[i][j-1]"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            if i == 0:
                dp[i] = [1] * (m + 1)
                continue
                
            for j in range(m + 1):
                if j == 0:
                    dp[i][j] = 0
                    continue
                    
                if t[i - 1] == s[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

                dp[i][j] += dp[i][j - 1]    # 注意这一句不要写到else里面去了
                    
        return dp[n][m]
