"""
1055. Shortest Way to Form String

From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target.
If the task is impossible, return -1.

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
"""


"""
solution 1: greedy + two pointers - O(st)
"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        conc = 0
        i = 0
        while i < len(target):
            lens = self._longest_continuous_substring(i, source, target)
            if lens == 0:
                return -1
            i += lens
            conc += 1
        return conc
    
    def _longest_continuous_substring(self, start_idx, s, t):
        """
        find the longest consinuous substring in t that is a subsequence of s
        return the lens of the continuous substring
        two pointers
        """
        lens = 0
        i = 0           # idx in s
        j = start_idx   # idx in t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                lens += 1
                i += 1
                j += 1
            else:
                i += 1
        return lens



"""
solution 2: greedyf + binary seach - O(tlog(s))
"""
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ch_to_idx = collections.defaultdict(list)     # ch --> idx
        for i, ch in enumerate(source):
            ch_to_idx[ch].append(i)
        
        conc = 1
        start_idx = 0       # start index for binary search in source
        for ch in target:
            if ch not in ch_to_idx:
                return -1
            
            idx_lst = ch_to_idx[ch]         # idx_lst is the list we are going to do binary search for ch
            if start_idx > idx_lst[-1]:     # if the binary search has to start at a index larger than the largest idx in idx_lst, 
                conc += 1                   # then we need to start over for another concatination
                start_idx = 0
                
            next_idx = self._binary_search(idx_lst, start_idx)
            start_idx = next_idx + 1

        return conc
    
    def _binary_search(self, idx_lst, target_idx):
        """
        binary search for the first idx in idx_lst that is larger/euqal than target_idx
        """
        start, end = 0, len(idx_lst) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if idx_lst[mid] >= target_idx:
                end = mid
            else:
                start = mid
        return idx_lst[start] if idx_lst[start] >= target_idx else idx_lst[end]
                
