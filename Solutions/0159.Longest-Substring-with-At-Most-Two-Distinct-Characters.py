159. Longest Substring with At Most Two Distinct Characters

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.



class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ch_to_cnt = collections.defaultdict(int)
        max_lens = 0
        i = 0
        for j in range(len(s)):
            ch_to_cnt[s[j]] += 1
            
            while i <= j and len(ch_to_cnt) > 2:
                ch_to_cnt[s[i]] -= 1
                if ch_to_cnt[s[i]] == 0:
                    del ch_to_cnt[s[i]]
                i += 1
                
            if len(ch_to_cnt) <= 2:
                max_lens = max(max_lens, j - i + 1)
                
        return max_lens
