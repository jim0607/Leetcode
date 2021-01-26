"""
248. Strobogrammatic Number III

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

Example:

Input: low = "50", high = "100"
Output: 3 
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
Note:
Because the range might be a large number, the low and high numbers are represented as string.
"""




"""
解法：每次都按照一个lens做backtrack. 每次添加next_ch都在curr_comb前面和后面添加
backtrack end consition: if len(curr_comb) == lens, check if curr_comb in range(low, high)
constraints on next_candidates: next_comb = ch + curr_comb + mapping[ch], cannot have leading zero
arguments pass into backtrack function: curr_comb
"""
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def backtrack(curr_comb, n):
            if len(curr_comb) == n:
                if int(low) <= int(curr_comb) <= int(high):
                    res.add(curr_comb)
                return
            
            for next_ch in mapping:
                next_comb = next_ch + curr_comb + mapping[next_ch]
                if len(next_comb) == n and next_comb[0] == "0":     # cannot have leading zero
                    continue
                backtrack(next_comb, n)       
        
        
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        res = set()
        for lens in range(len(low), len(high) + 1):    # 对于每一个lens, 做backtrack寻找等于lens的comb
            if lens % 2 == 0:       # 如果lens是偶数，那中间就没有ch
                backtrack("", lens)
            else:                   # 如果lens是奇数，中间只能是"0", "1", "8"
                backtrack("0", lens)
                backtrack("1", lens)
                backtrack("8", lens)
        return len(res)
