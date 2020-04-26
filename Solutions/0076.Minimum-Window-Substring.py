76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lens, lensTarget = len(s), len(t)
        
        if lens == 0 or lens < lensTarget:
            return ""
        
        targetDict, sourceDict = collections.defaultdict(int), collections.defaultdict(int)
        for char in t:
            targetDict[char] += 1
        
        res = ""
        minLen = float("inf")
        j = 0
        
        # 套用九章的模板
        for i in range(lens):
            while j < lens and not self.allIncluded(sourceDict, targetDict):
                sourceDict[s[j]] += 1
                j += 1
                
            if self.allIncluded(sourceDict, targetDict):
                if j - i < minLen:
                    minLen = j - i
                    res = s[i: j]
            
            sourceDict[s[i]] -= 1
            
        return res
    
    def allIncluded(self, sourceDict, targetDict):
        """
        return true if all the chars in target are included in source
        """
        for char, freq in targetDict.items():
            if freq > sourceDict[char]:
                return False 
            
        return True
