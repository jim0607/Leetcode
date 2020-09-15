"""
309. Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        
        hold = [float("-inf") for _ in range(len(prices))]
        unhold = [float("-inf") for _ in range(len(prices))]
        hold[0] = -prices[0]
        unhold[0] = 0
        hold[1] = max(-prices[0], -prices[1])
        unhold[1] = max(0, prices[1] - prices[0])
        
        for i in range(2, len(prices)):
            hold[i] = max(unhold[i-2] - prices[i], hold[i-1])
            unhold[i] = max(prices[i] + hold[i-1], unhold[i-1])
            
        return unhold[-1]
