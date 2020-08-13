326. Power of Three

Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false


"""
solution 1: recurssion
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 3:
            return False
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3)


"""
logx with base a = ( log x ) / ( log a ) 
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return abs(math.log(n, 3) - round(math.log(n, 3))) < 1e-10
