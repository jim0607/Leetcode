678. Valid Parenthesis String

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True


"""
Greedy: the whole idea is to check if "(" could be paired. Maintain two variables: cmin and cmax.
cmin is the minimum number of "(" that MUST be paired later.
cmax is the maximum number of "(" that COULD possibly be paired later.
After interate the while s, if cmin == 0 then return True.
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin, cmax = 0, 0
        for ch in s:
            if ch == "(":
                cmin += 1
                cmax += 1
                
            if ch == "*":
                cmin -= 1 if cmin > 0 else 0
                cmax += 1
                
            if ch == ")":
                cmin -= 1 if cmin > 0 else 0
                cmax -= 1
                if cmax < 0:        # meaning there are two many ")", even more than "("的数目加"*"的数目
                    return False    # cmax的唯一目的就在于这个提前return False
                
        return cmin == 0
            
            


"""
下面的想法是错的，需要规避。
"""
"""
只有一种括号，所以valid的条件是cnt == 0 at last and also cnt should never be negative.
加入了*, 那就是说只要有violation (cnt != 0 at last or cnt is negative somtime), 我们就用一个"*"去拯救一下。
但是过不了case: "(*)(", 因为出现在()里面的"*"也救不了后面(需要匹配的)
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt, cnt_star = 0, 0
        for ch in s:
            if ch == "(":
                cnt += 1
            if ch == ")":
                cnt -= 1
                if cnt < 0:
                    if cnt_star <= 0:
                        return False
                    else:
                        cnt_star -= 1
            if ch == "*":
                cnt_star += 1
                
        return cnt_star >= cnt
