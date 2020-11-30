3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             
             
# sliding window, tiem complexity: O(N)
# 维护一个included=set(), 用来记录i->j中include的char，套模板时满足的条件是s[j] not in included; 
# 更新j: included.add(s[j]); 更新i: included.remove(s[i])
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        included = set()
        j = 0
        max_lens = 0
        for i in range(len(s)):
            while j < len(s) and s[j] not in included:
                max_lens = max(max_lens, j - i + 1)
                included.add(s[j])
                j += 1
            
            included.remove(s[i])
            
        return max_lens
      
      
"""
也可以套用模板 for find max subarray size for at most problem 
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_to_cnt = collections.defaultdict(int)
        i = 0
        max_size = 0
        for j in range(len(s)):
            ch_to_cnt[s[j]] += 1
            
            while i <= j and not self._is_valid(ch_to_cnt):
                ch_to_cnt[s[i]] -= 1
                if ch_to_cnt[s[i]] == 0:
                    del ch_to_cnt[s[i]]
                i += 1
                
            if self._is_valid(ch_to_cnt):
                max_size = max(max_size, j - i + 1)
                
        return max_size
    
    def _is_valid(self, ch_to_cnt):
        for cnt in ch_to_cnt.values():
            if cnt > 1:
                return False
        return True
