"""
1025. Divisor Game

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
"""


"""
dp[i] = can he/she win facing i
"""
class Solution:
    def divisorGame(self, N: int) -> bool:
        if N <= 1:
            return False
        dp = [False for _ in range(N + 1)]
        dp[0] = False
        dp[1] = False
        dp[2] = True
        for j in range(3, N + 1):
            for x in range(1, j // 2 + 1):
                if not dp[j-x] and j % x == 0:
                    dp[j] = True
                    break
        return dp[N]
