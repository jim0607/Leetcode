"""
188. Best Time to Buy and Sell Stock IV

Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
"""



"""
O(N*K), O(K)
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or not prices:
            return 0
        
        # if k >= lens / 2, then the problem becomes 122, where you can make as much transactions as possible
        if k >= lens // 2:
            return self.stockII(prices)
        
        buy = [float("inf")] * k    # 第i次buy欠下的最小值
        sell = [0] * k              # 第i次sell赚下的最大值
        for price in prices:
            buy[0] = min(buy[0], price)                     # buy[0] = the minimum money you can own after the first purchase
            sell[0] = max(sell[0], price - buy[0])          # sell[0] = the maximum money you can earn after the first sell
            for i in range(1, k):
                buy[i] = min(buy[i], price - sell[i - 1])   # buy[i] = the minimum money you can own after the ith purchase
                sell[i] = max(sell[i], price - buy[i])      # sell[i] = the maximum money you can earn after the ith purchase
                
        return sell[-1]
   
    def stockII(self, prices: List[int]) -> int:
        prof = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                prof += prices[i] - prices[i-1]
        return prof

    
    
# solve the memory overflow problem below.
    
class Solution {
    public int maxProfit(int k, int[] prices) {
        int lens = prices.length;
        if (k == 0 || lens <= 1) return 0;
        
        // if k >= lens / 2, then the problem becomes 122, where you can make as much transactions as possible
        if (k >= lens / 2) {
            int maxPr = 0;
            for (int i = 1; i < lens; i++) {
                if (prices[i] > prices[i - 1]) {
                    maxPr += prices[i] - prices[i - 1];
                }
            }
            return maxPr;
        }

        // if k < lens / 2, then we don't need to worry about the memory overflow problem anymore
        int[] minPrice = new int[k];
        int[] maxProf = new int[k];
        for (int i = 0; i < k; i++) {
            minPrice[i] = Integer.MAX_VALUE;    // # note that this leads to memory reaches maximum error when k is large; that is why we do the above checking k > lens / 2
        }
        for (int price : prices) {
            minPrice[0] = Math.min(minPrice[0], price);
            maxProf[0] = Math.max(maxProf[0], price - minPrice[0]);
            for (int j = 1; j < k; j++) {
                minPrice[j] = Math.min(minPrice[j], price - maxProf[j - 1]);
                maxProf[j] = Math.max(maxProf[j], price - minPrice[j]);
            }
        }
        return maxProf[k - 1];
    }
}
