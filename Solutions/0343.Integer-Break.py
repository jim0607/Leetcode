"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. 
Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""



"""
拆分乘积最大的两个原则：1. 当所有拆分出的数字相等时，乘积最大； 2：拆分成三份时，乘积最大
证明：https://leetcode-cn.com/problems/integer-break/solution/343-zheng-shu-chai-fen-tan-xin-by-jyd/
o(1), O(1)
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        div, mod = n // 3, n % 3
        if mod == 0:
            return 3**div       
        elif mod == 1:
            return 4 * 3**(div - 1)     # 4*3*3
        elif mod == 2:
            return 6 * 3**(div - 1)     # 5*3*3 --> (2+3)*3*3
