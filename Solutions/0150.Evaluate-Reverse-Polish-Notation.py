"""
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_st = []
        for ch in tokens:
            if ch == "+":
                num_st.append(num_st.pop() + num_st.pop())
            elif ch == "-":
                num_st.append(-num_st.pop() + num_st.pop())
            elif ch == "*":
                num_st.append(num_st.pop() * num_st.pop())
            elif ch == "/":                         
                num_st.append(int(1 / num_st.pop() * num_st.pop()))   # Division between two integers should truncate toward zero, in python, 
                                                                      # we should note that 6//8 = 0, but 6/(-8) = -1. So we use int() to take the integer part of the float number. 
            else:       # if ch is a number
                num_st.append(int(ch))
                
        return num_st[0]
