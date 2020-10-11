"""
246. Strobogrammatic Number

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
Example 4:

Input: num = "1"
Output: true
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {"6": "9", "9": "6", "1": "1", "0": "0", "8": "8"}
        i, j = 0, len(num) - 1
        while i <= j:       # 注意这里要 <=
            if num[i] not in mapping or num[j] not in mapping:
                return False
            if mapping[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        return True
