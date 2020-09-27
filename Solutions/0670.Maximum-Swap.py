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
        

"""
solution 2: one pass from backward - O(N)
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = [ch for ch in str(num)]
        num_to_idx = collections.defaultdict(int)
        max_idx = len(s) - 1
        need_swap = [-1, -1]
        for i in range(len(s)-1, -1, -1):
            if s[i] > s[max_idx]:
                max_idx = i
            elif s[i] < s[max_idx]:     # 如果碰到一个小的，应该与后面已经遍历过的max_idx交换
                need_swap = (max_idx, i)    
        
        s[need_swap[0]], s[need_swap[1]] = s[need_swap[1]], s[need_swap[0]]
        return int("".join(s))
