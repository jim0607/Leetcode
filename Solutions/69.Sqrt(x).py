Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
             

# 方法一：二分法
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        start, end = 1, x
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid**2 >= x:
                end = mid
            else:
                start = mid
        if end**2 == x:
            return end
        else:
            return start  


# Newton's Method. O(logN) since the set converges quadratically.
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        y = x
        while y**2 - x >= 1:
            y = (y + x / y) / 2
        return int(y)
