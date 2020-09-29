"""
371. Sum of Two Integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)
        
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            while y:
                res = x ^ y     # 相同为1, 相异为0
                carry = (x & y) << 1
                x, y = res, carry
        else:
            while y:
                res = x ^ y
                borrow = ((~x) & y) << 1
                x, y = res, borrow
                
        return x * sign
