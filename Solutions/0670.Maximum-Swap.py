"""
670. Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
"""


"""
solution 2: one pass from backward 一路更新 max_ch_idx - O(N)
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = [ch for ch in str(num)]
        
        max_ch_idx = len(s) - 1
        swap = [0, 0]
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] > s[max_ch_idx]:
                max_ch_idx = idx
            elif s[idx] < s[max_ch_idx]:
                swap = [idx, max_ch_idx]
        
        s[swap[0]], s[swap[1]] = s[swap[1]], s[swap[0]]
        
        return int("".join(s))


"""
solution 1: sort and compare - O(nlogn)
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        num_to_idx = collections.defaultdict(int)
        for i, num in enumerate(s):
            num_to_idx[num] = i
        sorted_s = sorted(s, key = lambda x: -ord(x))
        res = [ch for ch in s]
        for i in range(len(s)):
            if s[i] != sorted_s[i]:
                idx = num_to_idx[sorted_s[i]]     # 找到arr中靠后的那个需要替换的idx  
                res[i], res[idx] = res[idx], res[i]
                break
        return int("".join(res))
