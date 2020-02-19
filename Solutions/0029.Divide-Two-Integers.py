Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2


"""https://www.youtube.com/watch?v=htX69j1jf5U"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) == (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        res = 0
        
        while a >= b:
            x = 0
            while a >= b << (x + 1):
                x += 1
            
            res += 1 << x
            a -= b << x
            
        return min(res if sign else -res, 2**31 - 1)
