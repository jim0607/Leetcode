"""
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


"""
solution: dfs 解法跟22. Generate parentheses是一样的，给你这么多括号，去生成所有的valid parentheses, 然后取其中最长的valid parentheses就可以了；
只能暴力generate出所有的valid parenthsis，每个括号都有可能加或不加进去，所以是O(2^N).
"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def backtrack(curr_idx, left_cnt, right_cnt, curr_comb):
            if curr_idx == len(s) - 1 and left_cnt == right_cnt:
                res.add(curr_comb)
                return
            
            if left_cnt > left_total or right_cnt > right_total:
                return
            if left_cnt < right_cnt:
                return
            
            for next_idx in range(curr_idx + 1, len(s)):
                if s[next_idx] == "(":
                    backtrack(next_idx, left_cnt, right_cnt, curr_comb)             # not add "(" to result
                    backtrack(next_idx, left_cnt + 1, right_cnt, curr_comb + "(")   # add "(" to result
                elif s[next_idx] == ")":
                    backtrack(next_idx, left_cnt, right_cnt, curr_comb)
                    backtrack(next_idx, left_cnt, right_cnt + 1, curr_comb + ")")
                else:                                  # if it is a letter, then simply put it into curr    
                    backtrack(next_idx, left_cnt, right_cnt, curr_comb + s[next_idx])
                
          
        left_total, right_total = 0, 0
        for ch in s:
            if ch == "(":
                left_total += 1
            elif ch == ")":
                right_total += 1
        
        res = set()
        backtrack(-1, 0, 0, "")
        
        ans = []
        max_len = max(len(comb) for comb in res)
        for comb in res:
            if len(comb) == max_len:
                ans.append(comb)
        return ans
    


"""
同样是dfs, 下面这种写法就不会TLE
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
                dfs(idx + 1, left + 1, right, left_remain - 1, right_remain, curr_path + "(")   # add "(" to result
                dfs(idx + 1, left, right, left_remain - 1, right_remain, curr_path)             # not add "(" to result
                
            elif s[idx] == ")":
                dfs(idx + 1, left, right + 1, left_remain, right_remain - 1, curr_path + ")")   # add ")" to result
                dfs(idx + 1, left, right, left_remain, right_remain - 1, curr_path)             # not add ")" to result
            
            else:                                                       # if it is a letter, then simply put it into curr
                dfs(idx + 1, left, right, left_remain, right_remain, curr_path + s[idx])        # add "a" to result
                
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
