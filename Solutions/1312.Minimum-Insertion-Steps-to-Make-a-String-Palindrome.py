"""
1312. Minimum Insertion Steps to Make a String Palindrome

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
Example 4:

Input: s = "g"
Output: 0
Example 5:

Input: s = "no"
Output: 1
 
Constraints:

1 <= s.length <= 500
All characters of s are lower case English letters.
"""


"""
题目其实是求 n - (the longest palindromic subsequence in s);
也就是 to find the longest common subsequence between s and s[::-1].
which is same as 1143.Longest Common- Subsequence.
eg: mbadm, 
    mdabm. 
The longest palindromic subsequence is mbm, 所以insertion steps = 5 - 3 = 2;
也就是通过insertion把a 和 d弄成palindromic: mdabadm
"""
class Solution:
    def minInsertions(self, s: str) -> int:
        return len(s) - self.longest_palind_subseq(s, s[::-1])
    
    def longest_palind_subseq(self, s, t):
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
