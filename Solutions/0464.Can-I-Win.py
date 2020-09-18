"""
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
"""




"""
solution 1: naive recursion - 指数级别复杂度
"""
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        if maxChoosableInteger >= desiredTotal:
            return True
        
        if any(not self.canIWin(maxChoosableInteger, desiredTotal - num) for num in range(1, maxChoosableInteger + 1)):
            return True
        
        return False
        

"""
solution 2: dfs + memo
"""
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def dfs(curr_total, curr_choosable):
            if len(curr_choosable) == 0:
                return False
            if curr_choosable[-1] >= curr_total:    # 如果可一次性拿走，那就赢了
                return True
            if curr_choosable in memo:
                return memo[curr_choosable]
            for i in range(len(curr_choosable)):
                if not dfs(curr_total - curr_choosable[i], curr_choosable[:i] + curr_choosable[i+1:]):
                    memo[curr_choosable] = True
                    return True
            memo[curr_choosable] = False
            return False
        
        
        # 一个数只能用一次，所以如果所有maxChoosableInteger都用了都加不到desiredTotal那就return False
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False
        
        memo = collections.defaultdict(bool)    # (curr_choosable_numbers --> can_win_with_curr_choosable_numbers?)
        return dfs(desiredTotal, tuple(range(1, maxChoosableInteger + 1)))  # 这里用了curr_choosable_numbers就不需要visited了
