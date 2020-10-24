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
        if n <= 1:
            return False
        
        possible_lens = []
        for i in range(2, n + 1):
            if n % i == 0:
                possible_lens.append(n // i)
        
        for lens in possible_lens:
            if self.check_valid(s, lens):
                return True
        return False
    
    def check_valid(self, s, k):
        substr = s[:k]
        for i in range(k, len(s), k):
            if s[i:i+k] != substr:
                return False
        return True
