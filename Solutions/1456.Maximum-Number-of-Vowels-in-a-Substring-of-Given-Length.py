"""
1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).


Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
"""


"""
套 sliding window with fixed size 模板即可
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        max_cnt = 0
        vowel_cnt = 0
        for i in range(len(s)):
            vowel_cnt += 1 if s[i] in vowels else 0         # step 1: 把ith item加进去
            
            if i >= k:
                vowel_cnt -= 1 if s[i-k] in vowels else 0   # step 2: 把(i-k)th item 吐出来
                
            max_cnt = max(max_cnt, vowel_cnt)               # step 3: 更新res
            
        return max_cnt
