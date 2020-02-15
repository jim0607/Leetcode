91. Decode Ways

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


"""
1423
if we want to know the decode ways to 3 (include 3), 我们可以从3那里划分，求出142的decode ways M个，也可以从2那里划分，求出14的decode ways N个. 那么decode ways to 3就有M+N个
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        # 搞这个多edge case何必呢，找踩么不是
        if not self.isValid(s[0]):
            return 0
        if len(s) == 1:
            return 1
        
        # 这个initialize 比较繁琐
        dp = [0] * len(s) 
        dp[0] = 1
        if self.isValid(s[1]):
            dp[1] = 2 if self.isValid(s[:2]) else 1
        else:
            dp[1] = 1 if self.isValid(s[:2]) else 0
            
        for i in range(2, len(s)):
            m, n = 0, 0
            if self.isValid(s[i]):
                m = dp[i - 1]
            if self.isValid(s[i -1:i + 1]):
                n = dp[i - 2]
                
            dp[i] = m + n
        
        return dp[-1]
    
    def isValid(self, s):
        if len(s) == 1:
            return True if 0 < int(s) <= 26 else False
        else:
            return True if 0 < int(s) <= 26 and int(s[0]) != 0 else False
            
"""经典的dp题，很容易想到。
不考虑繁琐的edge case的话，下面的code就是对的"""
class Solution:
    def numDecodings(self, s: str) -> int:
        lens = len(s)
        if lens <= 1:
            return lens
        dp = [0]*lens
        dp[0] = 1
        dp[1] = 1 if int(s[:1]) > 26 else 2
        for i in range(2, lens):
            if int(s[i-1:i+1]) <= 26:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[lens-1]
