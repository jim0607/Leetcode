188. Best Time to Buy and Sell Stock IV

Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.


"""O(N*K), O(K) memory error"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or not prices:
            return 0
        
        buy = [float("inf")] * k        # note that this leads to memory reaches maximum error when k is large
        sell = [0] * k
        for price in prices:
            buy[0] = min(buy[0], price)                     # buy[0] = the minimum money you can own after the first purchase
            sell[0] = max(sell[0], price - buy[0])          # sell[0] = the maximum money you can earn after the first sell
            for i in range(1, k):
                buy[i] = min(buy[i], price - sell[i - 1])   # buy[i] = the minimum money you can own after the ith purchase
                sell[i] = max(sell[i], price - buy[i])      # sell[i] = the maximum money you can earn after the ith purchase
                
        return sell[-1]
