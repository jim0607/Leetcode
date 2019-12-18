Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.


"""提示：Consider the first K stock prices. At the end, the only legal states are that you don't own a share of stock, or that you do. Calculate the most profit you could have under each of these two cases.
定义dp[i][0]为i天后手里有股票的最大收益，dp[i][1]为i天后手里没有股票的最大收益
递推关系：dp[i][0] = max(dp[i-1][1]-prices[i], dp[i-1][0])； dp[i][1] = max(dp[i-1][0]+prices[i]-fee, dp[i-1][1])
初始条件：dp[0][0], dp[0][1] = -prices[0], 0
返回值：max(dp[lens-1][0], dp[lens-1][1])"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        lens = len(prices)
        dp = [[0]*2 for _ in range(lens)]
        dp[0][0], dp[0][1] = -prices[0], 0
        for i in range(1, lens):
            dp[i][0] = max(dp[i-1][1]-prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0]+prices[i]-fee, dp[i-1][1])
        return max(dp[lens-1][0], dp[lens-1][1])
        
        
""" 这一题就解决了，但是这样处理 base case 很麻烦，而且注意一下状态转移方程，新状态只和相邻的一个状态有关，其实不用整个 dp 数组，只需要一个变量储存相邻的那个状态就足够了，这样可以把空间复杂度降到 O(1):"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        lens = len(prices)
        dp_0, dp_1 = -prices[0], 0
        for i in range(1, lens):
            temp = dp_0
            dp_0 = max(dp_1-prices[i], dp_0)
            dp_1 = max(temp+prices[i]-fee, dp_1)
        return max(dp_0, dp_1)
