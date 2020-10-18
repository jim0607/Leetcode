"""
583. Delete Operation for Two Strings

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, 
where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lens1, lens2 = len(word1), len(word2)
        
        # dp[i][j] = the min number of steps needed to make word1[:i] and word[:j] the same
        dp = [[0] * (lens2 + 1) for _ in range(lens1 + 1)]
        for i in range(lens1 + 1):
            dp[i][0] = i
        for i in range(lens2 + 1):
            dp[0][i] = i
            
        for i in range(1, lens1 + 1):               # 注意点1: 因为有buffer layer, 所以范围是(1, lens1 + 1)
            for j in range(1, lens2 + 1):
                if word1[i - 1] == word2[j - 1]:    # 注意点2: 注意有了buffer layer之后，dp中的i对应的是text中的i-1,所以判断条件是when A[i-1]=B[j-1]
                    dp[i][j] = dp[i - 1][j - 1]
                
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
                    
        return dp[lens1][lens2]

# 解法二非常巧妙！
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lens1, lens2 = len(word1), len(word2)
        
        LSC = self.longestCommonSubsequence(word1, word2)
        
        return lens1 - LSC + lens2 - LSC
       
    # below is the code copied from 1143 the LCS problem
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                   
        return dp[-1][-1]
