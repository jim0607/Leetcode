1208. Get Equal Substrings Within Budget

You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.
Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to charactor in t, so the maximum length is 1.
Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You can't make any change, so the maximum length is 1.



"""
step 1: construct a cost arr; step 2: sliding window to solve the problem of 
finding the max lens of subarry with sum at most target
"""
class Solution:
    def equalSubstring(self, s: str, t: str, max_cost: int) -> int:
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        
        i = 0
        cost = 0
        max_lens = 0
        for j in range(len(costs)):
            cost += costs[j]            # 更新前面指针的信息
            
            while i <= j and cost > max_cost:
                cost -= costs[i]        # 更新后面指针的信息
                i += 1
                
            max_lens = max(max_lens, j - i + 1)     # 更新res
            
        return max_lens
