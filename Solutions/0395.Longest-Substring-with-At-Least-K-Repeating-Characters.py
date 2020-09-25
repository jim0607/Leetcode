"""
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




"""
For each i in range(1, 27), use sliding window technique to find the longest substring to satisfy two conditions:
1. the number of total unique characters in substring is i;
2. at least k repeating characters.
第二种模板：find max subarray size for at most problem. 写法是while loop里让前面的指针去追后面的指针
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for i in range(1, 27):
            res = max(res, self._sliding_window(s, k, i))
        return res
    
    def _sliding_window(self, s, k, total_unique):
        """
        In a helper function, we do sliding window to find the longest substring that satisfy two conditions:
        1. the number of total unique characters in substring is i;
        2. at least k repeating characters
        第二种模板：find max subarray size for at most problem. 写法是while loop里让前面的指针去追后面的指针
        """
        curr_valid = 0      # 合格了的ch的个数
        curr_unique = 0     # unique ch的个数in the window = 合格了加上没有合格的ch的个数
        ch_to_cnt = [0 for _ in range(26)]
        max_lens = 0
        i = 0
        for j in range(len(s)):
            # step 1: 更新后面的指针
            if ch_to_cnt[ord(s[j]) - ord("a")] == 0:        # 更新curr_unique的个数
                curr_unique += 1
            ch_to_cnt[ord(s[j]) - ord("a")] += 1
            if ch_to_cnt[ord(s[j]) - ord("a")] == k:        # 更新合格了的ch个数
                curr_valid += 1
                
            # step 2: 更新前面的指针
            while i <= j and curr_unique > total_unique:    # move left pointer forwar to satisfy condition 1
                if ch_to_cnt[ord(s[i]) - ord("a")] == k:    # 更新合格了的ch个数
                    curr_valid -= 1
                ch_to_cnt[ord(s[i]) - ord("a")] -= 1
                if ch_to_cnt[ord(s[i]) - ord("a")] == 0:    # 更新curr_unique的个数
                    curr_unique -= 1
                i += 1
                
            # step 3: 更新res
            if curr_unique == curr_valid:           # meaning 没有不合格的ch了, satisfy condition 2
                max_lens = max(max_lens, j - i + 1)
                
        return max_lens




"""
solution 2: recursion
use those char which counting is smaller than k as a 'wall' to
divide the string into two parts and use recursion on the two parts.
O(26n)
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
