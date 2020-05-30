76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.


"""
below solution is easy, but time comsuming O(MN)
"""
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
        for i in range(lens):   # O(N)
            while j < lens and not self.allIncluded(sourceDict, targetDict):  # O(M)
                sourceDict[s[j]] += 1
                j += 1
                
            if self.allIncluded(sourceDict, targetDict):   
                if j - i < minLen:
                    minLen = j - i
                    res = s[i: j]    # O(N)
            
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
    
    
    
"""
this solution is O(N), instead of using self.allIncluded(sourceDict, targetDict) to check matched or not, 
we use a int missing to keep track of how many chars are still needed in order to match
also, in stead of using s[i:j] everytime we renew res, we use start, end to renew the idx, which reduce time from O(N) to O(1)
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(s) < len(t):
            return ""
        
        need = collections.Counter(t)  # store how many chars are needed, positive means needed, negative means have more chars than needed
        missing = len(t) # store how many chars are still missing in order to match, positive means we need more chars to match t, 0 means matched, same as self.allIncluded(sourceDict, targetDict) 
        start, end = 0, 0
        i, j = 0, 0
        res = ""
        
        for i in range(len(s)):
            while j < len(s) and missing > 0:
                if need[s[j]] > 0:  # if s[j] could be a valid add up in order to match t, then missing-1
                    missing -= 1
                need[s[j]] -= 1
                j += 1

            if missing == 0:    # instead of use self.allIncluded(sourceDict, targetDict) to check matched, we use missing == 0?
                if end == 0 or j-i < end-start:
                    start, end = i, j   # 也可以定义一个res, 用res = s[i:j]来更新结果，但是takes O(N)时间，所以用start, end来记录就可以了
                    
            if need[s[i]] == 0:
                missing += 1
            need[s[i]] += 1
                
        return s[start:end]
