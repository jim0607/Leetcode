567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

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
套用九章模板 O(M+N) if cnt1 == cnt2 is O(1)
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


       

"""
solution 2: sliding window with fix lens: O(M+M*(N-M))
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntDict = collections.defaultdict(int)
        for ch in s1:
            cntDict[ch] += 1
            
        for i in range(len(s2)-len(s1)+1):  # O(N-M)
            tempDict = collections.defaultdict(int)
            for ch in s2[i:i+len(s1)]:    # O(M)
                tempDict[ch] += 1

            if tempDict == cntDict:       # O(?)
                return True
            
        return False
