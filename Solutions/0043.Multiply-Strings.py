"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


"""
3 * 456 = 456 + 456 + 456
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 > num2:
            return self.multiply(num2, num1)
        
        n2 = 0
        for ch in num2:
            n2 = n2 * 10 + ord(ch) - ord("0")
        
        res = 0
        for ch in num1:
            temp = 0
            for _ in range(ord(ch) - ord("0")):     # 3 * 456 = 456 + 456 + 456
                temp += n2
            res = 10 * res + temp
        return str(res)
