301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]


"""
solution: dfs 解法跟22. Generate parentheses是一样的，给你这么多括号，去生成所有的valid parentheses, 然后取其中最长的valid parentheses就可以了；
只能暴力generate出所有的valid parenthsis，每个括号都有可能加或不加进去，所以是O(2^N).
"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        # idx is the idx in s, left, right are how many "(" and how many ")" are there in curr_path
        # left_remain is how many "(" remaining so that we can take from s to put into curr_path
        # curr_path is the valid parenethes we want to build
        def dfs(idx, left, right, left_remain, right_remain, curr_path):
            if idx == len(s) and left == right and left_remain == right_remain == 0:
                res.add(curr_path)
                return
            
            if idx >= len(s):
                return
            if left_remain < 0 or right_remain < 0:
                return
            if left < right:    # 借鉴了22. Generate parentheses
                return
            
            if s[idx] == "(":       
                if left_remain > 0:
                    dfs(idx + 1, left + 1, right, left_remain - 1, right_remain, curr_path + "(")   # add "(" to result
                dfs(idx + 1, left, right, left_remain - 1, right_remain, curr_path)                 # not add "(" to result
                
            elif s[idx] == ")":
                if right_remain > 0:
                    dfs(idx + 1, left, right + 1, left_remain, right_remain - 1, curr_path + ")")   # add ")" to result
                dfs(idx + 1, left, right, left_remain, right_remain - 1, curr_path)                 # not add ")" to result
            else:
                dfs(idx + 1, left, right, left_remain, right_remain, curr_path + s[idx])            # add "a" to result
                
        res = set()
        
        left_cnt, right_cnt = 0, 0
        for ch in s:
            if ch == "(":
                left_cnt += 1
            elif ch == ")":
                right_cnt += 1
                
        dfs(0, 0, 0, left_cnt, right_cnt, "")
        
        max_lens = max(len(s) for s in res)
        ans = []
        for s in res:
            if len(s) == max_lens:
                ans.append(s)
                
        return ans
