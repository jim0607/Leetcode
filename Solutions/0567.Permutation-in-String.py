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
solution 1: sliding window O(M+26*(N-M))
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntDict = collections.defaultdict(int)
        for ch in s1:
            cntDict[ch] += 1
            
        for i in range(len(s2)-len(s1)+1):
            tempDict = collections.defaultdict(int)
            for ch in s2[i:i+len(s1)]:
                tempDict[ch] += 1

            if tempDict == cntDict:
                return True
            
        return False
