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
solution: use two hashmaps to record the frequency of word.
O(len(s)*len(words)*len(words[0]))
"""
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        lens = len(s)
        word_len = len(words[0])
        word_num = len(words)
        word_freq = collections.Counter(words)
        res = []
        for i in range(lens - word_len * word_num + 1):             # O(len(s))
            seen = collections.defaultdict(int)
            for j in range(i, i + word_len * word_num, word_len):   # O(len(words)*len(words[0]))
                curr_word = s[j:j+word_len]                         
                if curr_word not in word_freq:
                    break
                seen[curr_word] += 1
                if seen[curr_word] > word_freq[curr_word]:
                    break
                
            if word_freq == seen:
                res.append(i)
                
        return res
