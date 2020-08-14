395. Longest Substring with At Least K Repeating Characters

Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.



"""
use those char which counting is smaller than k as a 'wall' to
divide the string into two parts and use recursion on the two parts.
O(26N)
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        return self._helper(s, k, 0, n)
    
    def _helper(self, s, k, start, end):
        if end - start < k:
            return 0
        
        freq = collections.defaultdict(int)
        for i in range(start, end):
            freq[s[i]] += 1
        
        # 如果所有的cnt都大于k, 那么return end-start
        if all(cnt >= k for cnt in freq.values()): return end - start
            
        # 如果不是所有的cnt都大于k, 那么找到那个不大于k的ch, 在他的左右两边做divide and conquer
        for ch in freq:
            if freq[ch] < k:
                for i in range(start, end):
                    if s[i] == ch:
                        left = self._helper(s, k, start, i)
                        right = self._helper(s, k, i+1, end)
                        return max(left, right)
