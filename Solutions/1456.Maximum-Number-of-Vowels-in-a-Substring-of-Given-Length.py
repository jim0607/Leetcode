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


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = 0
        vowels = {"a", "e", "i", "o", "u"}
        for i in range(k):
            if s[i] in vowels:
                cnt += 1
                
        max_cnt = cnt
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                cnt += 1
            if s[i-k] in vowels:
                cnt -= 1
            max_cnt = max(cnt, max_cnt)
            
        return max_cnt
