"""
1216. Valid Palindrome III

Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
"""




"""
find the Longest Palindromic Subsequence L, return lens - L <= k.
"""
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        return len(s) - self.longestPalin(s) <= k
    
    # below is just 516. Longest Palindromic Subsequence
    def longestPalin(self, s):
        dp = [[1 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j == i + 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]
