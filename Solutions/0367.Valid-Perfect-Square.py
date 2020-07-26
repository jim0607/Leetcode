367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(math.sqrt(num))**2 == num
        
        
"""
follow up: Do not use any built-in library function such as sqrt.
binary search - O(logN) or Newton's method - O(logN)
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 1, num
        while start + 1 < end:
            mid = start + (end - start) // 2
            if num > mid**2:
                start = mid
            else:
                end = mid
        return True if start**2 == num or end**2 == num else False
