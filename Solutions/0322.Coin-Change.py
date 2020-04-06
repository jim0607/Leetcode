You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

"""方法一：自下而上，时间复杂度：O(S*n)。空间复杂度：O(S)，dp 使用的空间。"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)      # # dp[i]表示amount = i时最少的组合方法数
        dp[0] = 0                               # 初始条件
        for num in range(1, amount + 1):        # 注意for循环里不要包含初始条件
            for coin in coins:
                if num - coin >= 0:             # 这里判断num-coin>=0是为了防止越界
                    dp[num] = min(dp[num - coin] + 1, dp[num])
                
        return dp[-1] if dp[-1] != float("inf") else -1
    
    
    
public class Solution {
    public int CoinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];    // dp[x] = the minimum amount of coin in order to sum up to x
        for (int i = 1; i < dp.Length; i++) {
            dp[i] = int.MaxValue;
        }
        
        for (int num = 1; num < dp.Length; num++) {
            foreach (int coin in coins) {
                // must check dp[num - coin] != int.MaxValue otherwise int.MaxValue + 1 in the next line will become int.MinValue, something different for C#
                if (num >= coin && dp[num - coin] != int.MaxValue) {  
                    dp[num] = Math.Min(dp[num - coin] + 1, dp[num]);
                }
            }
        }
        
        return dp[dp.Length - 1] == int.MaxValue ? -1 : dp[dp.Length - 1];
    }
}

"""还有BFS,DFS的算法，后面可以多思考一下"""
