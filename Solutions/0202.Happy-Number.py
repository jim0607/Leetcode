"""
202. Happy Number

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""



"""
solution 1: 用一个hashset记录number, if next number is in visited, 说明成环了，就return False - O(N), O(N);
solution 2: slow, fast双指针往前跑，fast跑两步，如果slow == fast说明成环了，return False - O(N), O(1).
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while fast != 1 and self._get_next(fast) != 1:
            slow = self._get_next(slow)                 # slow 走一步
            fast = self._get_next(self._get_next(fast)) # fast 走两步
            if slow == fast:    # 如果成环了，那就return False
                return False
        return True
        
    def _get_next(self, num):
        """
        Return the next number for num
        """
        res = 0
        while num > 0:
            res += (num % 10) ** 2
            num = num // 10
        return res
