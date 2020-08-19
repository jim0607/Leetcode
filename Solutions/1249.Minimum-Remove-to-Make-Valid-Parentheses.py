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
solution 1: use a st to store "(". 
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        res = ""
        for ch in s:
            if ch == "(":
                st.append(ch)
                res += ch
                
            elif ch == ")":
                if len(st) != 0:    # if not st, we don't append ")" to res
                    st.pop()
                    res += ch
            else:
                res += ch

        # if there is still "(" left in st, we delete them form the end of the string
        ans = []
        i = len(res) - 1
        while i >= 0 and len(st) > 0:
            if res[i] == "(":   # if it is "(", then we don't append it to ans
                st.pop()
            else:
                ans.append(res[i])
            i -= 1
                
        ans.append(res[:i+1])
        
        return "".join(ans[::-1])
 
 
 
"""
solution 2: 借鉴32. Longest Valid Parentheses的做法：first sweep left to right, and store the ")" that should be deleted, eg: "())", the last ")" should be deleted;
then sweep right to left, and store "(" that should be deleted, eg: eg: "(()", the first "(" should be deleted; 
lastly delete the prarentheses that should be deleted.
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left, right = 0, 0
        pos = set()     # store the pos where a parentheses should be deleted
        
        # first sweep left to right, and store the ")" that should be deleted, eg: "())", the last ")" should be deleted
        for i, ch in enumerate(s):
            if ch == "(":
                left += 1
            elif ch == ")":
                right += 1
            if right > left:
                pos.add(i)
                right -= 1
                
        # then sweep right to left, and store "(" that should be deleted, eg: eg: "(()", the first "(" should be deleted
        left, right = 0, 0
        for i, ch in enumerate(s[::-1]):
            if ch == "(":
                left += 1
            elif ch == ")":
                right += 1
            if left > right:
                pos.add(len(s) - i - 1)     # 注意这里不是add(i)
                left -= 1
                
        # then delete the prarentheses that should be delted
        res = ""
        for i, ch in enumerate(s):
            if i in pos:
                continue
            res += ch
            
        return res
