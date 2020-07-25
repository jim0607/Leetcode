294. Flip Game II

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:

Input: s = "++++"
Output: true 
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
Follow up:
Derive your algorithm's runtime complexity.



"""
dfs+memo: O(N^2)
memo[(curr_s)] = 能稳赢
"""
class Solution:
    def canWin(self, s: str) -> bool:
        def dfs(curr_s, memo):
            if self._garantee_to_lose(curr_s):
                return False
            
            if curr_s in memo:
                return memo[curr_s]

            for next_s in self._find_next(curr_s):
                memo[curr_s] = memo[curr_s] or (not dfs(next_s, memo))  # 只要有一个next的dfs(next)稳输那就curr就稳赢
                                                                        # 所以这里用 or 
            return memo[curr_s]
        
        memo = collections.defaultdict(lambda: False)   # 注意这里的初始化成False
        return dfs(s, memo)
        
    def _garantee_to_lose(self, s):
        found = False       
        for i in range(1, len(s)):             
            if s[i-1] == "+" and s[i] == "+":
                found = True
        return not found    # 没有连着两个"++"那就稳输
    
    def _find_next(self, s):
        res = []
        for i in range(1, len(s)):
            if s[i-1] == "+" and s[i] == "+":
                res.append(s[:i-1] + "--" + s[i+1:])
        return res
