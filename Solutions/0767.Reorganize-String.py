767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""



"""
I think it is similar with task schedule.  always put the most freq ch adjacent with the 2nd most freq ch.
We can firstly find the freq, and then put them into a heapq,
then each time we pop the most freq one, and also pop to get the second most freq one.
after using them, their freq-=1 and we push them back.
O(Nlogk), where N is total number of ch, K is total number of distinct number.
"""
import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        freq = collections.Counter(S)
        hq = []
        for ch, cnt in freq.items():
            heapq.heappush(hq, (-cnt, ch))
            
        res = ""
        while hq:
            most_freq_cnt, most_freq_ch = heapq.heappop(hq)
            most_freq_cnt *= -1
            if not hq:
                return res + most_freq_ch * most_freq_cnt if most_freq_cnt <= 1 else ""
            
            second_most_freq_cnt, second_most_freq_ch = heapq.heappop(hq)
            second_most_freq_cnt *= -1
            
            res += most_freq_ch + second_most_freq_ch
            
            most_freq_cnt -= 1
            second_most_freq_cnt -= 1
            
            if most_freq_cnt != 0:
                heapq.heappush(hq, (-most_freq_cnt, most_freq_ch))
            if second_most_freq_cnt != 0:
                heapq.heappush(hq, (-second_most_freq_cnt, second_most_freq_ch))
                
        return res
