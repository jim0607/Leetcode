921. Minimum Add to Make Parentheses Valid

Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

 

Example 1:

Input: "())"
Output: 1
Example 2:

Input: "((("
Output: 3
Example 3:

Input: "()"
Output: 0
Example 4:

Input: "()))(("
Output: 4


"""
借鉴32. Longest Valid Parentheses的做法：从左往右扫描，记录left和right，
如果right大于left了,就表明前面需要添加right-left个左括号
"""
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left, right = 0, 0
        cnt = 0
        for ch in S:
            if ch == "(":
                left += 1
            if ch == ")":
                right += 1
                
            if right >= left:
                cnt += right - left
                left, right = 0, 0
                
        cnt += left- right
        
        return cnt
