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




class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        minDist = float("inf")
        idx1, idx2 = -1, -1
        if word1 != word2:
            for i, word in enumerate(words):
                if word == word1:
                    idx1 = i
                if word == word2:
                    idx2 = i
                
                if idx1 != -1 and idx2 != -1:
                    minDist = min(minDist, abs(idx1 - idx2))
        
        else:
            prev, curr = -1, -1
            for i, word in enumerate(words):
                if word == word1:
                    curr = i
                    if prev != -1:
                        minDist = min(minDist, curr - prev)
                    prev = curr
                    
        return minDist
