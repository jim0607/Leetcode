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
sort the words by lens, and check the word one by one to see if there is a match.
How to check if word matches s? use two pointers to traverse word and s, compare as they go.
O(n*k*logn + n*m), where n is the lens of words, k is the average lens of word in words, m is the lens of s
"""
class Solution:
    def findLongestWord(self, s: str, words: List[str]) -> str:
        words.sort(key = lambda word: (-len(word), word))   # 按word的长度排序，按word的字母顺序排序O(n*k*logn)
        for word in words:
            idx1, idx2 = 0, 0
            while idx1 < len(s) and idx2 < len(word):
                if s[idx1] == word[idx2]:
                    idx1 += 1
                    idx2 += 1
                else:
                    idx1 += 1
            
            if idx2 == len(word):
                return word
            
        return ""
