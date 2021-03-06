"""
1056. Confusing Number

Given a number N, return true if and only if it is a confusing number, which satisfies the following condition:

We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. 
When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. 
A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

Example 1:

Input: 6
Output: true
Explanation: 
We get 9 after rotating 6, 9 is a valid number and 9!=6.
Example 2:

Input: 89
Output: true
Explanation: 
We get 68 after rotating 89, 86 is a valid number and 86!=89.
Example 3:

Input: 11
Output: false
Explanation: 
We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number.
Example 4:

Input: 25
Output: false
Explanation: 
We get an invalid number after rotating 25.
"""


class Solution:
    def confusingNumber(self, N: int) -> bool:
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        s = str(N)
        if any(ch for ch in s if ch not in mapping): return False
        rotated = ""
        for i in range(len(s) - 1, -1, -1):
            rotated += mapping[s[i]]
        return rotated != s

    
class Solution:
    def confusingNumber(self, N: int) -> bool:
        mapping = {6: 9, 9: 6, 8: 8, 1: 1, 0: 0}
        
        digits = []
        while N != 0:
            mod = N % 10
            if mod not in mapping:
                return False
            digits.append(mod)
            N //= 10
        
        r_digits = []
        for i in range(len(digits) - 1, -1, -1):
            r_digits.append(mapping[digits[i]])

        return r_digits != digits
