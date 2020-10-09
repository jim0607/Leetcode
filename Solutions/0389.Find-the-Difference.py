"""
389. Find the Difference

You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
Example 3:

Input: s = "a", t = "aa"
Output: "a"
Example 4:

Input: s = "ae", t = "aea"
Output: "a"
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnter_s = collections.Counter(s)
        cnter_t = collections.Counter(t)
        for ch, cnt in cnter_t.items():
            if ch not in cnter_s or cnt > cnter_s[ch]:
                return ch
