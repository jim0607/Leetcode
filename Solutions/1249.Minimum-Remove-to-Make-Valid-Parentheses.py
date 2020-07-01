1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"


"""
借鉴32. Longest Valid Parentheses的做法：first sweep left to right, and store the ")" that should be deleted, eg: "())", the last ")" should be deleted;
then sweep right to left, and store "(" that should be deleted, eg: eg: "(()", the first "(" should be deleted; 
lastly delete the prarentheses that should be deleted.
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left, right = 0, 0
        idx = set()    # store the idx where a parentheses should be deleted
        
        # first sweep left to right, and store the ")" that should be deleted, eg: "())", the last ")" should be deleted
        for i, ch in enumerate(s):
            if ch == "(":
                left += 1
            if ch == ")":
                right += 1
            if right > left:
                idx.add(i)
                right -= 1
        
        # then sweep right to left, and store "(" that should be deleted, eg: eg: "(()", the first "(" should be deleted
        left, right = 0, 0
        for i, ch in enumerate(s[::-1]):
            if ch == ")":
                right += 1
            if ch == "(":
                left += 1
            if left > right:
                idx.add(len(s) - i - 1)
                left -= 1

        # then delete the prarentheses that should be delted
        res = ""
        i, j = 0, 0
        while i < len(s):
            if i in idx:
                idx.remove(i)
                i += 1
                continue
                
            res += s[i]
            i += 1
            
        return res
