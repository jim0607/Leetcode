358. Rearrange String k Distance Apart

Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.



"""
similar with task schedule, 我们按频率从大到小去坐k个位置，pop出来之后需要将freq-=1然后push回去
"""
from heapq import heappush, heappop

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 0: return s     # edge case
        
        freq = collections.Counter(s)        
        hq = []
        for ch, cnt in freq.items():
            heappush(hq, (-cnt, ch))
            
        res = ""
        while hq:
            add_back = []
            for _ in range(k):
                if hq:      # pop 之前要确定不为空
                    cnt, ch = heappop(hq)
                    res += ch
                    cnt *= -1
                    cnt -= 1
                    if cnt > 0:
                        add_back.append((cnt, ch))
                        
                else:
                    return res if not add_back else ""
   
            for cnt, ch in add_back:
                heappush(hq, (-cnt, ch))
                    
        return res
