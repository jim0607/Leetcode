Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


    
"""
recursion solution: O(logN)
"""    
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        
        res = 0.0
        
        half = self.myPow(x, n//2)     # 用一个half避免重复计算 self.myPow(x, n//2) * self.myPow(x, n//2) 中需要计算self.myPow(x, n//2)两次
        
        if n%2 == 0:
            res = half * half
        else:
            res = half * half * x
        
        return res 
    

    
    
    
    

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x == -1:
            return 1 if n % 2 == 0 else -1
        
        k = n if n > 0 else -n
        x = x if n > 0 else 1 / x
        res = 1
        while k >= 1:
            mod = k % 2
            div = k // 2
            if mod == 0:
                res *= x**div
            else:
                res *= x**div * x
                
            k = div
                
        return res
