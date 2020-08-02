8. String to Integer (atoi)

Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.



"""
we only need to handle 3 cases:
1. discards all leading whitespaces - using python str.strip(char)
2. sign of the number - use 正负1来代表符号
3. overflow
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        # The strip() method returns a copy of the string by removing both the leading and 
        # the trailing characters (based on the string argument passed).
        s = s.strip()
        
        sign = 1    # 用正负1来代表符号，直接相乘就可以了
        res = 0
        num_found = False       # whether the first number has been found
        sign_found = False      # whether the first sign has been found
        for ch in s:
            if ch == "+":
                if num_found or sign_found:   # if already found a number or sign, then this sign is not valid
                    break
                sign_found = True
                sign = 1
                
            elif ch == "-":
                if num_found or sign_found:
                    break
                sign_found = True
                sign = -1
                
            elif ch.isdigit():
                num_found = True
                res = 10 * res + (ord(ch) - ord("0"))    # 注意不能用int(ch)来cheating
                
            else:       # 如果是字母以及其他字符，说明num结束了
                break
        
        if sign == 1:
            return min(res, 2**31 - 1)  # 处理越界的数
        else:
            return max(-res, -2**31)
