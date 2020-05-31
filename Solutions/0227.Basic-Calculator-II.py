227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.

"""
不用stack, 用四根指针prevNum, prevSign, currNum, currSign
"""
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        prevNum, prevSign = 0, "+"
        currNum, currSign = 0, "+"
        i = 0
        while i < len(s):
            if s[i].isdigit():
                currNum = ord(s[i]) - ord("0")
                while i+1 < len(s) and s[i+1].isdigit():
                    currNum = currNum * 10 + ord(s[i+1]) - ord("0")
                    i += 1
                print(i, currNum)
                if prevSign == "+":
                    res += prevNum
                    print(i, prevNum, res)
                    prevNum = currNum
                elif prevSign == "-":
                    res += prevNum
                    prevNum = -currNum
                elif prevSign == "*":   # not update res, combine preVal & curVal and keep loop
                    prevNum *= currNum
                    print(prevNum)
                elif prevSign == "/":
                    prevNum = int(prevNum / currNum) 
            
            i += 1
            if i < len(s) and s[i] in ["+", "-", "*", "/"]:
                prevSign = s[i]
                
        return res + prevNum
