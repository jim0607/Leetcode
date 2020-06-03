243. Shortest Word Distance

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


""" Solution 1: simliar with brutal force.  O(N*(L1+L2)) """
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx1, idx2 = [], []
        for i, word in enumerate(words):    # O(N) where N is the # of words
            if word == word1:       # O(L1) where L1 is the length of word1 
                idx1.append(i)
            if word == word2:
                idx2.append(i)
                
        idx1.sort()     # O(MlogM) where M is the number of duplicated word1 in words
        idx2.sort()
        i, j = 0, 0
        minDist = abs(idx1[i]-idx2[j])
        while i < len(idx1) and j < len(idx2):
            if idx1[i] > idx2[j]:
                j += 1
            else:
                i += 1
            if i < len(idx1) and j < len(idx2):
                minDist = min(minDist, abs(idx1[i]-idx2[j]))
                
        return minDist
        
        
""" Solution 2: simliar with solution 1 except for only one pass.  O(N*(L1+L2)) """
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx1, idx2 = -1, -1
        minDist = float("inf")
        for i, word in enumerate(words):    # O(N) where N is the # of words
            if word == word1:       # O(L1) where L1 is the length of word1 
                idx1 = i
            if word == word2:
                idx2 = i
            
            if idx1 != -1 and idx2 != -1:
                minDist = min(minDist, abs(idx1-idx2))
        
        return minDist
