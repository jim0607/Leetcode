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

# @lc code=start
import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        heapq.heappush(heap, 1)
        seen = set()
        seen.add(1)
        
        for _ in range(n):
            currMin = heapq.heappop(heap)
            
            for num in [2, 3, 5]:
                newNum = currMin * num
                
                if newNum not in seen:
                    heapq.heappush(heap, newNum)
                    seen.add(newNum)
                    
        return currMin
        
        
# @lc code=end
