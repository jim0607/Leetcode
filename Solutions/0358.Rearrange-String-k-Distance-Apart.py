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
"""
we always want to seat the high freq char first, so we maintain a max hq to enable fast abtain of maxfreq.
we seat the high freq first, then the 2nd highest freq.... 
if at some point, we need to seat a char to maintain k distance, 
but hq is empty meaning cannot seat any more chars, we return False 
"""
from heapq import *

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 0: return s     # edge case
        
        freqs = collections.Counter(s)
        hq = []
        for ch, freq in freqs.items():
            heappush(hq, (-freq, ch))
            
        res = ""
        addback = []
        while len(hq) > 0:  # len(hq) means there are still chars needed to be located
            for _ in range(k):      # let chars sit on k seats one by one
                if len(hq) == 0:    # 没有char可放了
                    return res if len(addback) == 0 else ""  # addback也为空的话表示所有的char已经安放完了
                                                             # 这时候就可以提前退出了
                freq, ch = heappop(hq)
                freq = -freq
                freq -= 1
                if freq > 0:
                    addback.append((-freq, ch))
                    
                res += ch
                
            while len(addback) > 0:
                heappush(hq, addback.pop())
                
        return res
