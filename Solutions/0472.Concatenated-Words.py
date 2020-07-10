472. Concatenated Words

Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
        
        
        
"""
solution 1: dfs - TLE
"""   
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        word_set = set(words)

        for word in words:
            if self._dfs(word_set, word, word):
                res.append(word)
                
        return res
    
    def _dfs(self, word_set, word, curr_word):
        if len(curr_word) < len(word) and curr_word in word_set:
            return True
        
        for i in range(1, len(curr_word)):
            prefix = curr_word[:i]
            suffix = curr_word[i:]
            if self._dfs(word_set, word, prefix) and self._dfs(word_set, word, suffix):
                return True
            
        return False
        

"""
solution 2: dfs + memorization - Top down DP
"""
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        word_set = set(words)
        memo = collections.defaultdict(bool)    # defaultdict里面必须传入val的类型

        for word in words:
            if self._dfs(word_set, word, word, memo):
                res.append(word)
                
        return res
    
    def _dfs(self, word_set, word, curr_word, memo):
        if len(curr_word) < len(word) and curr_word in word_set:
            return True
        
        if curr_word in memo:
            return memo[curr_word]
        
        memo[curr_word] = False
        for i in range(1, len(curr_word)):
            prefix = curr_word[:i]
            suffix = curr_word[i:]
            if self._dfs(word_set, word, prefix, memo) and self._dfs(word_set, word, suffix, memo):
                memo[curr_word] = True
                return True
                
        return False
        
        
        

"""
另一种写法的 dfs - O(MN + NlogN) where N = len(words), M = average len(word)
"""
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        words.sort(key = lambda word: len(word))    # 先按照长度排个序，这样后面的一定比前面的长
        word_set = set()
        for word in words:
            if self._is_valid(word_set, word):
                res.append(word)
            word_set.add(word)
                
        return res
    
    def _is_valid(self, word_set, word):
        if word in word_set:  # 因为排了序后面的一定比前面的长，所以这里可以check
            return True
        
        for i in range(1, len(word)):
            if word[:i] in word_set and self._is_valid(word_set, word[i:]):
                return True
            
        return False
