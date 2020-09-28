"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""



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
        return end if end**2 <= x else start


# Newton's Method. O(logN) since the set converges quadratically.
cclass Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = x
        while sqrt*sqrt - x >= 1:
            sqrt = (sqrt + x / sqrt) / 2
            
        return int(sqrt)
      
      
"""
Gradient descent solution. 
If we keep out learning rate alpha to be a constant ie. 1, the time complexity will be O(x).
Since we boost the gradient descent by "Adaptive Learning Rates" method - keep reducing steps by half,
the time complexity will be O(logx)
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x <= 3:
            return 1
        
        return self.gradient_descent(x)
    
    def gradient_descent(self, x):
        y = 0                                       # start from 0, not x
        alpha = x / 2                               # steps to take at each iteration
        gradient = self.calculate_gradient(x, y)    # gradient at each iteration
        while abs(y**2 - x) >= 0.1:                 # alpha * gradient is the decay rate
            alpha = alpha / 2          # boost the gradient descent by "Adaptive Learning Rates" method - keep reducing steps by half
            gradient = self.calculate_gradient(x, y)
            y -= alpha * gradient

        return int(y + 1) if int(y + 1)**2 == x else int(y)
    
    def calculate_gradient(self, x, y):
        cost_func = y**2 - x                 # use MSE as cost function, gradient = d(cost) / dx
        return 1 if cost_func > 0 else -1    # gradient is which way we should go - increase res of decrease res
