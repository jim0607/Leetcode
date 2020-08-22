#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (38.40%)
# Likes:    1290
# Dislikes: 78
# Total Accepted:    127.3K
# Total Submissions: 331.3K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#

from heapq import *

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        hq = [1]
        included = set()
        included.add(1)
        for _ in range(n - 1):
            currmin = heappop(hq)
            if 2 * currmin not in included:
                heappush(hq, 2 * currmin)
                included.add(2 * currmin)
            if 3 * currmin not in included:
                heappush(hq, 3 * currmin)
                included.add(3 * currmin)
            if 5 * currmin not in included:
                heappush(hq, 5 * currmin)
                included.add(5 * currmin)
            
        return heappop(hq)
