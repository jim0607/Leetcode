"""
392. Is Subsequence

Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.
"""


"""
solution 1: two pointers
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        i, j = 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == m


"""
Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, 
and you want to check one by one to see if T has its subsequence. 
In this scenario, how would you change your code?
"""
"""
binary search: O(mlogn)
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ch_to_idx = collections.defaultdict(list)
        for idx, ch in enumerate(t):
            ch_to_idx[ch].append(idx)
        
        start_idx = 0
        for ch in s:
            if ch not in ch_to_idx:
                return False
            if start_idx > ch_to_idx[ch][-1]:
                return False
            
            idx_lst = ch_to_idx[ch]
            next_idx = self._binary_search(idx_lst, start_idx)
            start_idx = next_idx + 1
            
        return True
    
    def _binary_search(self, idx_lst, target_idx):
        """
        return the idx that is just larger than the target_idx
        """
        start, end = 0, len(idx_lst) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if idx_lst[mid] < target_idx:
                start = mid
            else:
                end = mid
        return idx_lst[start] if idx_lst[start] >= target_idx else idx_lst[end]
