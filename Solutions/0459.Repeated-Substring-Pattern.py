"""
459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


"""
step 1: find all possible divisible lens - O(n^0.5); step 2: try each possible divisible lens to see is it's a valid divide - O(n^1.5).
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for lens in range(1, n // 2 + 1):      # there are n^0.5 possible lens, each check takes O(n)
            if n % lens == 0 and self.check_possible(s, lens):
                return True
        return False
    
    def check_possible(self, s, lens):
        sub = s[:lens]
        for i in range(0, len(s), lens):
            if s[i:i+lens] != sub:
                return False
        return True
