"""
524. Longest Word in Dictionary through Deleting

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
"""



"""
sort the words by lens, and check the word one by one to see if there is a match.
How to check if word matches s? use two pointers to traverse word and s, compare as they go.
O(n*k*logn + n*m), where n is the lens of words, k is the average lens of word in words, m is the lens of s
"""
class Solution:
    def findLongestWord(self, s: str, arr: List[str]) -> str:
        arr.sort(key = lambda x: (-len(x), x))  # 按word的长度排序，按word的字母顺序排序O(n*k*logn)
        for t in arr:
            if len(t) > len(s):     # skip strings that are too long
                continue
            if self._is_valid(s, t):
                return t
        return ""
    
    def _is_valid(self, s, t):
        """
        Return if we can change s to t by deleting some chars in s
        """
        m, n = len(s), len(t)
        i, j = 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return True if j == n else False
