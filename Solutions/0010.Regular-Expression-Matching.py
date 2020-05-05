Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".


"""f[i][j]=A前i个字符A[0..i)和B前j个字符B[0..j)能否匹配
情况一：B[j-1]不是"*": f[i][j] = f[i-1][j-1] if (B[j-1]="." or A[i-1]=B[j-1])
情况二：B[j-1]是"*"：可以让"*"表示0个前面的字符，那就让A[0..i)去和B[0..j-2)匹配： f[i][j] = f[i][j-2]；也可以让"*"表示几个前面的字符，A[i-1]是多个ch中的最后一个，能否匹配取决于A[0..i-1)和B[0..j)是否匹配：f[i][j] = f[i-1][j] if (B[j-2]="." or B[j-2]=A[i-1])"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
            
        if m == 0 and n == 0:
            return True
        if n == 0:
            return False
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
            
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue
                    
                if j == 0:
                    dp[i][j] = False
                    continue
                    
                if p[j - 1] != "*":
                    if i >= 1 and (p[j - 1] == "." or s[i - 1] == p[j - 1]):
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    if j >= 2:
                        dp[i][j] = dp[i][j] or dp[i][j - 2]     # 为什么减2呢？因为"ac*" 如果*代表0个c的话，就变成了"a"
                        
                    if j >= 2 and i >= 1:
                        if p[j - 2] == "." or s[i - 1] == p[j - 2]:
                            dp[i][j] = dp[i][j] or dp[i - 1][j]
                
        return dp[m][n]
