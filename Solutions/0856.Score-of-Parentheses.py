856. Score of Parentheses

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6

"""
stack is good for parentheses problems
"""
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res = 0
        st = [0]         # store how many "(" needs to be paired and the res so far
        for i in range(1, len(S)):
            if S[i] == "(":
                st.append(0)    # "(" 表示开始新一轮的计算了
            if S[i] == ")":
                top = st.pop()
                if st:
                    if S[i - 1] == ")":
                        st[-1] += 2 * top
                    else:
                        st[-1] += top + 1
                else:           # 如果为空了表示到目前为止左括号和右括号匹配了，也就是"()()"前面两个括号处理完了 
                    if S[i - 1] == ")":
                        res += 2 * top
                    else:
                        res += top + 1
                        
        return res
