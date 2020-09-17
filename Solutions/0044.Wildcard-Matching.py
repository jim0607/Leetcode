"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
"""



"""
f[i][j]=A前i个字符A[0..i)和B前j个字符B[0..j)能否匹配
画个图会很明了，详见九章算法动态规划双序列型DP。
情况一：B[j-1]不是"*": f[i][j] = f[i-1][j-1] if (B[j-1]="?" or A[i-1]=B[j-1])
情况二：B[j-1]是"*"：可以让"*"表示0个字符，那就让A[0..i)去和B[0..j-1)匹配： f[i][j] = f[i][j-1]；
也可以让"*"表示字符，A[i-1]肯定是多个ch中的最后一个，能否匹配取决于A[0..i-1)和B[0..j)是否匹配：f[i][j] = f[i-1][j]
"""
cclass Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        if p == "*": return True
        if m == 0 and n == 0: return True
        if m == 0 or n == 0: return False
        
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue
                if j == 0:
                    dp[i][j] = False
                    continue
                if p[j-1] == "*":
                    dp[i][j] = dp[i][j-1]   # "*" represen nothing
                    if i >= 1:
                        dp[i][j] = dp[i][j] or dp[i-1][j]  # "*" represen a seq, and the seq has to end with s[i-1]
                else:
                    if p[j-1] == "?" or (i >= 1 and p[j-1] == s[i-1]):
                        dp[i][j] = dp[i-1][j-1]
                        
        return dp[m][n]
