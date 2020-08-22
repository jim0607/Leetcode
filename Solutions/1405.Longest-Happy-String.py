1405. Longest Happy String

A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 2, b = 2, c = 1
Output: "aabbc"
Example 3:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.


"""
有点像621. Task Schedule. 用一个hq保存最大的freq, 然后按要求排座位，注意add_back.
突然觉得task schdule每次都优先排最大的freq这个做法非常greedy. 
heapq 本身就是greedy, 每次都有选择性地pop出来，Dijkstra就是一个例子，
对于这题，我们先判断把最high freq的ch pop出来加入res, 然后freq-1放回hq中
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hq = []
        if a > 0: heappush(hq, (-a, "a"))
        if b > 0: heappush(hq, (-b, "b"))
        if c > 0: heappush(hq, (-c, "c"))
        
        res = ""
        addback = []
        while len(hq) > 0:
            freq, ch = heappop(hq)
            
            # case 1: if there are already to same ch on top of res
            # then we cannot seat this ch, instead, we seat the 2nd highest freq
            if len(res) >= 2 and res[-1] == ch and res[-2] == ch:
                if len(hq) == 0:    # 养成好习惯，在heappop之前判断不为空
                    return res
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
