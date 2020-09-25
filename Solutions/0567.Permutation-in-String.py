"""
567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""


"""
solution 1: 由于我们要求的substring时固定长度的，所以最好maintina a fixed size window - 套用fix window模板
"""
class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        k = len(s2)
        counter2 = collections.Counter(s2)
        ch_to_cnt = collections.defaultdict(int)
        for i in range(len(s1)):
            ch_to_cnt[s1[i]] += 1   # fixed window模板: step 1: 把ith item加到window
         
            if i >= k:              # maintian a fixed size window - 把(i-k)th item 吐出来
                ch_to_cnt[s1[i-k]] -= 1
                if ch_to_cnt[s1[i-k]] == 0:
                    del ch_to_cnt[s1[i-k]]
                    
            if ch_to_cnt == counter2:  # step 3: update res
                return True
            
        return False




"""
套用九章模板
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = collections.Counter(s1)
        cnt2 = collections.Counter()
            
        j = 0
        for i in range(len(s2)):
            while j < len(s2) and j - i < len(s1):
                cnt2[s2[j]] += 1
                j += 1
            
            if cnt1 == cnt2:
                return True
            
            cnt2[s2[i]] -= 1
            if cnt2[s2[i]] == 0:
                del cnt2[s2[i]]
            
        return False
