340. Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.


# 维护一个charDict, 用来记录i->j中的char的频率，套模板时满足的条件是len(charDict) <= k; 
# 更新j: charDict[s[j]+=1; 更新i: charDict[s[i]] -= 1, if charDict[s[i]] == 0: del charDict[s[i]]
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        lens = len(s)
        if lens == 0 or k == 0:
            return 0
        
        charDict = collections.defaultdict(int)
        
        j = 0
        res = 0
        # 套用模板即可
        for i in range(lens):
            while j < lens and len(charDict) <= k:
                if s[j] not in charDict and len(charDict) == k:  # 保证不再加了，再加就满了
                    break
                    
                charDict[s[j]] += 1   # 更新 j
                j += 1
            
            # if 满足条件, 跟新res
            if len(charDict) <= k:
                res = max(res, j - i)
            
            # 更新 i
            charDict[s[i]] -= 1
            if charDict[s[i]] == 0:
                del charDict[s[i]]
            
        return res
