123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
             

class Solution {
    public int maxProfit(int[] prices) {
        int buy1 = Integer.MAX_VALUE;   // the minimum money you can own after the 1st buy
        int sell1 = 0;                  // the max money you can earn after the 1st sell
        int buy2 = Integer.MAX_VALUE;
        int sell2 = 0;
        for (int price : prices) {
            buy1 = Math.min(buy1, price);
            sell1 = Math.max(sell1, price - buy1);
            buy2 = Math.min(buy2, price - sell1);
            sell2 = Math.max(sell2, price - buy2);
        }
        return Math.max(sell1, sell2);
    }
}


//Same as above, but more similar with 121.  This algorithm is just 121 algorithm repeating twice

class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;   // the minimum money you can own after the 1st buy
        int maxProf = 0;                    // the max money you can earn after the 1st sell
        int minPrice_2 = Integer.MAX_VALUE;
        int maxProf_2 = 0;
        for (int price : prices) {
            minPrice = Math.min(minPrice, price);
            maxProf = Math.max(maxProf, price - minPrice);
            minPrice_2 = Math.min(minPrice_2, price - maxProf);
            maxProf_2 = Math.max(maxProf_2, price - minPrice_2);
        }
        return maxProf_2;
    }
}
