309. Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]



class Solution {
    public int maxProfit(int[] prices) {
        int lens = prices.length;
        if (lens <= 1) return 0;
        
        int[] hold = new int[lens];     // hold[i] = the max profit if there is stock in hand on day i
        int[] unhold = new int[lens];   // unhold[i] = the max profit if there isn't stock in hand on day i
        hold[0] = -prices[0];
        unhold[0] = 0;
        hold[1] = Math.max(-prices[0], -prices[1]);
        unhold[1] = Math.max(0, prices[1] - prices[0]);
        
        for (int i = 2; i < lens; i++) {
            hold[i] = Math.max(hold[i - 1], unhold[i - 2] - prices[i]);
            unhold[i] = Math.max(hold[i - 1] + prices[i], unhold[i - 1]);
        }
        
        return unhold[lens - 1];
    }
}
