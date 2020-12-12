"""
123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = -sys.maxsize    # the max profit with the first buy
        sell1 = -sys.maxsize   # the max profit with the first sell
        buy2 = -sys.maxsize 
        sell2 = -sys.maxsize 
        
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, price + buy1)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, price + buy2)
            
        return max(sell1, sell2)
      


"""O(N), O(1) solution using DP"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell1, sell2 = 0, 0
        buy1, buy2 = float("inf"), float("inf")
        for price in prices:
            buy1 = min(price, buy1)             # buy1 = the minimum money you can 欠下 after the first purchase
            sell1 = max(sell1, price - buy1)    # sell1 = the maximum money you can 挣下 for the first sell
            buy2 = min(buy2, price - sell1)     # buy2 = the minimum money you can 欠下 after the second purchase
            sell2 = max(sell2, price - buy2)    # sell2 = the maximum money you can 挣下 after the second purchase
            
        return sell2
