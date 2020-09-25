"""
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
    

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cntDict = collections.defaultdict(int)  # key is string, val is how many times the key appears
        for ch in s:
            cntDict[ch] += 1
        
        for ch in t:
            cntDict[ch] -= 1
            
        for val in cntDict.values():
            if val != 0:
                return False
            
        return True
