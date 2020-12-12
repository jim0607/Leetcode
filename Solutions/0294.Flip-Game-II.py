"""
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


"""
dfs+memo: O(N^2)
memo = (curr_state-->guarantee a win)
"""
class Solution:
    def canWin(self, s: str) -> bool:
        def dfs(curr_s):
            """
            return can curr_s garantee a win
            """
            if curr_s in memo:
                return memo[curr_s]
            
            garantee_win = False
            for next_s in one_move(curr_s):
                if not dfs(next_s):     # 只要有一个next的dfs(next)稳输那就curr就稳赢
                    garantee_win = True
                    break
            
            memo[curr_s] = garantee_win
            return garantee_win
                
                
        def one_move(s):    # just copied Flip Game I to get next state
            res = []
            for i in range(1, len(s)):
                if s[i-1] == s[i] == "+":
                    res.append(s[:i-1] + "--" + s[i+1:])
            return res

        
        memo = defaultdict(bool)     # curr_s --> can curr_s garantee a win
        return dfs(s)





class Solution:
    def canWin(self, s: str) -> bool:
        def dfs(curr_state):
            if len(self.generatePossibleNextMoves(curr_state)) == 0:
                return False
            if curr_state in memo:
                return memo[curr_state]
            garantee_win = False
            for next_state in self.generatePossibleNextMoves(curr_state):
                garantee_win = garantee_win or not dfs(next_state)   # 只要有一个next的dfs(next)稳输那就curr就稳赢
            memo[curr_state] = garantee_win
            return garantee_win
        
        memo = collections.defaultdict(lambda: False)    # (curr_state-->guarantee a win)
        return dfs(s)

    # below just copied Flip Game I to get next state
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        res = []
        for i in range(1, len(s)):
            if s[i] == s[i-1] == "+":
                res.append(s[:i-1] + "--" + s[i+1:])
        return res
