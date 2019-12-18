A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


"""经典的dp题，很容易想到。"""
class Solution:
    def numDecodings(self, s: str) -> int:
        lens = len(s)
        if lens <= 1:
            return lens
        dp = [0]*lens
        dp[0] = 1
        dp[1] = 1 if int(s[:1]) > 26 else 2
        for i in range(2, lens):
            if int(s[i-1:i]) <= 26:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[lens-1]
