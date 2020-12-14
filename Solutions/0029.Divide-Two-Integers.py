"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
"""



"""
https://www.youtube.com/watch?v=htX69j1jf5U
eg: 10//3, 每次都右移几次3 << k, 相当于3x2x2x2...,直到3x2x2x2...>10, 然后取余数继续这个算法是O(logN)
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0) == (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        
        res = 0
        while a >= b:
            shift = 0       # shift多少次就是乘以多少次2
            while a >= (b << (shift + 1)):
                shift += 1
                
            res += 1 << shift
            a -= b << shift
            
        return min(res if sign else -res, 2**31-1)
