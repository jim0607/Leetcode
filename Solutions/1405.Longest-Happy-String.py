"""
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


"""
这种间隔k个位置安排座位的问题，都是task schedule的做法！
与767. Reorganize String是同一题，只是767不能连续两个相同，这个题不能连续三个相同，
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        cnter = {"a": a, "b": b, "c": c}
        hq = []
        for ch, freq in cnter.items():
            if freq > 0:
                heappush(hq, (-freq, ch))
            
        res = ""
        add_back = []
        while len(hq) > 0:
            first_freq, first_ch = heappop(hq)
            
            # case 1: if there are already two same ch on top of res
            # then we cannot seat the 1st_freq ch, instead, we seat the 2nd highest freq ch
            if len(res) >= 2 and res[-1] == first_ch and res[-2] == first_ch:
                if len(hq) == 0:        # 养成好习惯，在heappop之前判断不为空
                    return res          # 在case 1中只能加入second_freq ch, 但是有没有second_freq可加了
                                        # 那就表示1st_freq ch 加不进去了，直接return res
                second_freq, second_ch = heappop(hq)
                second_freq = -second_freq
                second_freq -= 1
                if second_freq > 0:
                    add_back.append((-second_freq, second_ch))  # 不要忘了addback
                res += second_ch
                
                add_back.append((first_freq, first_ch))         # 不要忘了addback 没有用上的the 1st freq, ch
                
            # case 2: if we can  seat ch into res, then go ahead and seat it it
            else:
                first_freq = -first_freq
                first_freq -= 1
                if first_freq > 0:
                    add_back.append((-first_freq, first_ch))
                res += first_ch
                    
            while len(add_back) > 0:
                heappush(hq, add_back.pop())

        return res
