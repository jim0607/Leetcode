"""
245. Shortest Word Distance III

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.
"""



class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        min_dist = float("inf")
        if word1 == word2:
            prev, curr = float("inf"), float("inf")
            for i, word in enumerate(words):
                if word == word1:
                    if curr == float("inf"):
                        curr = i
                    else:
                        prev = curr
                        curr = i
                        min_dist = min(min_dist, abs(curr - prev))
        else:
            idx1, idx2 = float("inf"), float("inf")
            for i, word in enumerate(words):
                if word == word1:
                    idx1 = i
                    min_dist = min(min_dist, abs(idx2 - idx1))
                elif word == word2:
                    idx2 = i
                    min_dist = min(min_dist, abs(idx2 - idx1))
        return min_dist
