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
dp[i][j] = is s[i to j including i and j] a palindrome?
dp[i][j] = True if dp[i+1][j-1] is True and s[i]==s[j].
if it is True, then number of palindromic substring += 1
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            cnt += 1
            
        for j in range(1, n):   # we need j-1 infomation to update j, 所以正序遍历
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    if j - i <= 2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        cnt += 1
                        
        return cnt
