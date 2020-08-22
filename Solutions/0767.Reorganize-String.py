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
这种间隔k个位置安排座位的问题，都是task schedule的做法！这一题k=1.
用一个hq保存最大的freq, 然后按要求排座位，注意add_back.
突然觉得task schdule每次都优先排最大的freq这个做法非常greedy. 
heapq 本身就是greedy, 每次都有选择性地pop出来，Dijkstra就是一个例子，
对于这题，我们先判断把最high freq的ch pop出来加入res, 然后freq-1放回hq中
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        freqs = collections.Counter(s)
        hq = []
        for ch, freq in freqs.items():
            if freq > (len(s) + 1) // 2:
                return ""
            heappush(hq, ((-freq, ch)))
            
        res = ""
        while len(hq) > 0:
            freq, ch = heappop(hq)
            
            # case 1: if there is already to same ch on top of res
            # then we cannot seat the 1st_freq ch, instead, we seat the 2nd highest freq
            if len(res) > 0 and ch == res[-1]:
                if len(hq) == 0:   # 养成好习惯，在heappop之前判断不为空
                    return ""      # 在case 1中只能加入second_freq ch, 但是有没有second_freq可加了
                                   # 那就表示1st_freq ch 加不进去了, return impossible
                second_freq, second_ch = heappop(hq)
                res += second_ch
                second_freq = -second_freq
                second_freq -= 1
                if second_freq > 0:         # 不要忘了addback
                    heappush(hq, (-second_freq, second_ch))
                heappush(hq, (freq, ch))    # 不要忘了addback 没有用上的the 1st freq, ch
                
            # case 2: if we can put seat ch into res, then go ahead and seat it it
            else:
                res += ch
                freq = -freq
                freq -= 1
                if freq > 0:
                    heappush(hq, (-freq, ch))
                    
        return res
