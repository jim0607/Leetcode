438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".




from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCnt = Counter(p)       # O(M)
        sCnt = Counter()
        
        res = []
        j = 0
        for i in range(len(s)):     # 套用九章模板
            while j < len(s) and j - i < len(p):   # O(1)
                sCnt[s[j]] += 1
                j += 1

            if sCnt == pCnt:    # O(?)
                res.append(i)
            
            sCnt[s[i]] -= 1
            if sCnt[s[i]] == 0:
                del sCnt[s[i]]
            
        return res
