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
        freq = collections.defaultdict(int)
        max_len = 0
        j = 0
        for i in range(len(s)):
            while j < len(s) and len(freq) <= 2:
                if s[j] not in freq and len(freq) == 2:
                    break
                freq[s[j]] += 1
                j += 1
                
            if len(freq) <= 2:
                max_len = max(max_len, j - i)
                
            freq[s[i]] -= 1
            if freq[s[i]] == 0:
                del freq[s[i]]
                
        return max_len
