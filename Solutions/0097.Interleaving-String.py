"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
"""

"""
f[i][j]=s3的前[0..i+j)个字符能否由s1前i个字符[0..i)和s2前j个字符[0..j)交错形成
f[i][j]=True when (s3[i+j-1]=s1[i-1] 且 f[i-1][j]=True 即s3的前[0..i+j-1)个字符能否由s1前i-1个字符[0..i-1)和s2前j个字符[0..j)交错形成) or (s3[i+j-1]=s2[j-1] and f[i][j-1]=True)
"""
"""
dp[i][j]=can form?
dp[i][j]=true if s1[i-1]==s3[i+j-1] and dp[i-1][j]=true; or if s2[j-1]==s3[i+j-1] and dp[i][j-1]=true
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if len(s3) != m + n: return False
        
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):   # 注意点1: 因为有buffer layer, 所以范围是(1, lens1 + 1)
            if s1[i-1] == s3[i-1]:  # 注意点2: 注意有了buffer layer之后，dp中的i对应的是text中的i-1,所以判断条件是when A[i-1]=B[j-1]
                dp[i][0] = dp[i-1][0]
        for j in range(1, n + 1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                    dp[i][j] = True
                if s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                    dp[i][j] = True
                    
        return dp[m][n]
