"""
58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        i = 0
        while i < len(s):
            if s[i].isalpha():
                j = i
                while j + 1 < len(s) and s[j+1].isalpha():  # 这个一定要熟练掌握
                    j += 1
                res = j - i + 1
                i = j
            i += 1
        return res
