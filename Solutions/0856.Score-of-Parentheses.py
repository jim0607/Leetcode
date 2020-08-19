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
solution 1: use a ch_st to store left parentheses. use num_st to stores res, num_st初始化一个0进去垫底。
if ch == "(": num_st.append(0); else: 弹出top of num_st 并更新 num_st[-1].
通过比较ch与prev_ch来判断是乘以2还是加上1
"""
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ch_st = []
        num_st = [0]
        prev_ch = ""
        for ch in S:
            if ch == "(":
                ch_st.append("(")
                num_st.append(0)
                
            else:
                ch_st.pop()
                top = num_st.pop()
                if prev_ch == ")":
                    top *= 2
                elif prev_ch == "(":
                    top += 1
                num_st[-1] += top
            
            prev_ch = ch
            
        return num_st[-1]
 
 
"""
solution 2: 题目说the string is balanced, so we don't need a ch_st.
"""
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res = 0
        st = [0]         # store how many "(" needs to be paired and the res so far, 初始化先放一个dummy val进去垫底
        for i in range(len(S)):
            if S[i] == "(":
                st.append(0)        # "(" 表示开始新一轮的计算了
                
            if S[i] == ")":
                top = st.pop()
                if S[i - 1] == ")":
                    st[-1] += 2 * top
                else:
                    st[-1] += top + 1
                        
        return st[-1]
