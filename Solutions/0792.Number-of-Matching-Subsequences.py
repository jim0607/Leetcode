"""
792. Number of Matching Subsequences

Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
"""


"""
compare each word with source string using two pointers.
O(nmk), where n = len(s), m = len(words) and k = average lens of word in words. TLE
"""
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        for word in words:
            if self._match(word, s):
                res += 1
        return res
    
    def _match(self, word, s):
        """
        return if word is a subsequence of s - two pointers
        """
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(word)
        
        
"""
Follow up: what if n is very large? can you make is faster?
use binary search in s.  O(mklogn)
"""
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ch_to_idx = defaultdict(list)
        for i, ch in enumerate(s):
            ch_to_idx[ch].append(i)
            
        res = 0
        for word in words:
            start_idx = 0               # start_idx for binary search in s
            can_find_every_ch = True    # can find every ch_of_word in s
            for ch in word:
                if ch not in ch_to_idx:
                    can_find_every_ch = False
                    break
                
                idx_lst = ch_to_idx[ch]     # the index list we are going to do binary search in
                if start_idx > idx_lst[-1]: # 如果在start_idx后面就找不到ch了
                    can_find_every_ch = False
                    break
                    
                idx = bisect.bisect_left(idx_lst, start_idx)
                start_idx = idx_lst[idx] + 1
                
            if can_find_every_ch:           # 每一个ch in word都在s中找到了
                res += 1
                
        return res
    
    
    
    
    
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ch_to_idx = defaultdict(list)
        for i, ch in enumerate(s):
            ch_to_idx[ch].append(i)
            
        res = 0
        for word in words:
            start_idx = 0               # start_idx for binary search in s
            can_find_every_ch = True    # can find every ch_of_word in s
            for ch in word:
                if ch not in ch_to_idx:
                    can_find_every_ch = False
                    break
                
                idx_lst = ch_to_idx[ch]     # the index list we are going to do binary search in
                if start_idx > idx_lst[-1]: # 如果在start_idx后面就找不到ch了
                    can_find_every_ch = False
                    break
                    
                idx = self.binary_search(idx_lst, start_idx)
                start_idx = idx + 1
                
            if can_find_every_ch:           # 每一个ch in word都在s中找到了
                res += 1
                
        return res
    
    def binary_search(self, lst, num):
        start, end = 0, len(lst) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if lst[mid] >= num:
                end = mid
            else:
                start = mid
        return lst[start] if lst[start] >= num else lst[end]
