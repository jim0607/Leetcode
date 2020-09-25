"""
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
"""



"""
solution 1: 由于我们要求的substring时固定长度的，所以最好maintina a fixed size window.
"""
class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        k = len(s2)
        counter2 = collections.Counter(s2)
        ch_to_cnt = collections.defaultdict(int)
        for i in range(len(s1)):
            ch_to_cnt[s1[i]] += 1
            if i >= k:              # maintian a fixed size window
                ch_to_cnt[s1[i-k]] -= 1
                if ch_to_cnt[s1[i-k]] == 0:
                    del ch_to_cnt[s1[i-k]]
                    
            if ch_to_cnt == counter2:
                return True
            
        return False


    
"""
solution 2: 套用sliding window模板
"""
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
