"""
30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. 
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""



"""
solution: use two hashmaps to record the frequency of word.
O(len(s)*len(words)*len(words[0]))
"""
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m, n = len(words[0]), len(words)        
        res = []
        counter = collections.Counter(words)
        
        for i in range(len(s) - m*n + 1):                   # O(len(s))
            if counter == self._get_cnt(s, i, i + m*n, m):  # O(m*n)
                res.append(i)
        return res
    
    def _get_cnt(self, s, start, end, m):
        word_to_cnt = collections.defaultdict(int)
        i = start
        while i < end:
            word_to_cnt[s[i:i+m]] += 1
            i += m
        return word_to_cnt
      
      
      
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m, n = len(words), len(words[0])
        target_cnter = Counter(words)
        res = []
        for j in range(n):
            cnter = defaultdict(int)
            for i in range(j, len(s), n):
                cnter[s[i:i+n]] += 1
                
                if i - j >= m * n:
                    cnter[s[i-m*n: i-m*n+n]] -= 1
                    if cnter[s[i-m*n: i-m*n+n]] == 0:
                        del cnter[s[i-m*n: i-m*n+n]]
                        
                if cnter == target_cnter:           
                    res.append(i - m * n + n)
            
        return res
