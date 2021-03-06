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
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] if p[j-1] == "*" else False
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                    
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    
                else:
                    if p[j-1] == s[i-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = False
                        
        return dp[-1][-1]
