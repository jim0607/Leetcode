  
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


class Solution {
    public int maxProfit(int[] prices, int fee) {
        int lens = prices.length;
        if (lens <= 1) return 0;
        
        int[] hold = new int[lens];         // hold[i] = the max profit with stock in hand on the ith day
        int[] unhold = new int[lens];
        hold[0] = -prices[0];
        unhold[0] = 0;
        
        for (int i = 1; i < lens; i++) {
            hold[i] = Math.max(hold[i - 1], unhold[i - 1] - prices[i]);
            unhold[i] = Math.max(unhold[i - 1], hold[i - 1] + prices[i] - fee);
        }
        
        return unhold[lens - 1];
    }
    
    
    
    
class Solution {
    public int maxProfit(int[] prices, int fee) {
        int lens = prices.length;
        if (lens <= 1) return 0;
        
        int hold = -prices[0];
        int unhold = 0;
        
        for (int i = 1; i < lens; i++) {
            int tempHold = hold;
            int tempUnhold = unhold;
            hold = Math.max(tempHold, tempUnhold - prices[i]);
            unhold = Math.max(tempUnhold, tempHold + prices[i] - fee);
        }
        
        return unhold;
    }
}
}
