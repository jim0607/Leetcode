224. Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23



"""
if it's a digit, should use a while loop to add the num in case there are multiple digits, eg: 322 - 16
if it's a sign, then convert to 1 or -1
if it's a (, then append the previous res and sign into the resStack and signStack, and initialize the sign and num for calculation inside the ()
if it's a ), then pop the resStack and signStack and update res
"""
class Solution:
    def calculate(self, s: str) -> int:
        resStack = []
        signStack = []
        res = 0
        num, sign = 0, 1
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = ord(s[i]) - ord("0")
                while i + 1 < len(s) and s[i+1].isdigit():      # 注意这里最好是去判断s[i+1] 而不是判断s[i]
                    num = num * 10 + ord(s[i+1]) - ord("0")
                    i += 1
                res += num * sign

            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
                
            elif s[i] == "(":
                resStack.append(res)    # save the res before () into a stack
                signStack.append(sign)
                res, sign = 0, 1     # should initialze the res and sign for the coming calculaton inside the ()
                
            elif s[i] == ")":
                res = resStack.pop() + res * signStack.pop()    # numStack.pop() is the res before the (),  res is the res in the (), signStack is the sign in front of the ()
                
            i += 1
                
        return res
