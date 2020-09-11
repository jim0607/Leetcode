"""
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

        
        
"""
solution 1: check each word to see if they can satisfy wordBreak I. - O(NM^2)
"""
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        res = []
        for word in word_set:       # takes O(N), where N is len(words)
            if not word:
                continue
            word_set.remove(word)
            if self._wordBreak(word, word_set):
                res.append(word)
            word_set.add(word)
        return res
            
            
    def _wordBreak(self, s, word_set) -> bool:   # takes O(M^2), where M is lens of word
        dp = [False for _ in range(len(s) + 1)] 
        dp[0] = True
        for j in range(len(dp)):
            for i in range(j-1, -1, -1): 
                if dp[i] and s[i:j] in word_set:   
                    dp[j] = True
                    break
        return dp[-1]
       
       

"""
solution 2: dfs + memorization - O(MN^2 + NlogN) where N = len(words), M = average len(word)
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
    
    def _is_valid(self, word_set, word):   # O(M^2)
        if word in word_set:  # 因为排了序后面的一定比前面的长，所以这里可以check
            return True
        
        for i in range(1, len(word)):
            if word[:i] in word_set and self._is_valid(word_set, word[i:]):
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
        
        
  
