424. Longest Repeating Character Replacement

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.


"""
Given a string convert it to a string with all same characters with minimal changes. 
The answer is (length of the entire string) - (number of times of the maximum occurring character in the string).
Given this, this problem is to find the max_lens of substring so that 
(length of substring - number of times of the maximum occurring character in the substring) is at most K.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = collections.defaultdict(int)
        max_lens = 0
        j = 0
        max_occur_freq = 0
        for i in range(len(s)):
            while j < len(s) and j - i - max_occur_freq <= k:
                freq[s[j]] += 1
                max_occur_freq = max(max_occur_freq, freq[s[j]])
                j += 1
            
            if j - i - max_occur_freq <= k:
                max_lens = max(max_lens, j - i)
            
            if freq[s[i]] == max_occur_freq:
                max_occur_freq - 1
            freq[s[i]] -= 1

        return max_lens
