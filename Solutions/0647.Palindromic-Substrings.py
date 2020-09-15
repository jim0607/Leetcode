"""
647. Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""


"""
dp[i][j] = is s[i to j including i and j] a palindrome?
dp[i][j] = True if dp[i+1][j-1] is True and s[i]==s[j].
if it is True, then number of palindromic substring += 1
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j == i + 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
        
        cnt = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if dp[i][j]:
                    cnt += 1
        return cnt
