394. Coins in a Line

There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.

Could you please decide the first player will win or lose?

If the first player wins, return true, otherwise return false.


"""f[i]=面对i个石子，先手是必胜还是必败
f[i]=True if f[i-1] or f[i-2]都是False
f[1]=f[2]=True"""
class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        if n == 0:
            return False
            
        if n <= 2:
            return True
            
        dp = [True] * (n + 1)
        dp[0] = dp[1] = dp[2] = True
        
        for i in range(3, n + 1):
            if not dp[i - 1] or not dp[i - 2]:
                dp[i] = True
                
            else:
                dp[i] = False
                
        return dp[n]

Solution 2: 数学规律法
class Solution:
    def firstWillWin(self, n):
        return n % 3 != 0
