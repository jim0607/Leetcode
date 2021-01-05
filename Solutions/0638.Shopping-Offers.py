"""
638. Shopping Offers

In LeetCode Store, there are some kinds of items to sell. Each item has a price.

However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.

You are given the each item's price, a set of special offers, and the number we need to buy for each item. The job is to output the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers.

Each special offer is represented in the form of an array, the last number represents the price you need to pay for this special offer, other numbers represents how many specific items you could get if you buy this offer.

You could use any of special offers as many times as you want.

Example 1:
Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation: 
There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
Example 2:
Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
Output: 11
Explanation: 
The price of A is $2, and $3 for B, $4 for C. 
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
You cannot add more items, though only $9 for 2A ,2B and 1C.
Note:
There are at most 6 kinds of items, 100 special offers.
For each item, you need to buy at most 6 of them.
You are not allowed to buy more items than you want, even if that would lower the overall price.
"""


"""
solution 1: backtrack - 套用backtrack模板，backtrack加入的参数有(curr_bought, curr_cost).
backtrack结束条件是if all(curr_bought[i] >= needs[i] for i in range(len(needs))).
backtrack的剪枝很重要 - skip deals that exceed needs: if any(special[i] > needs[i] - curr_bought[i] for i in range(len(needs)))
O(2^M*L*N) where L is len(prices), M is how many specials are there, N is value of needs
"""
class Solution:
    def shoppingOffers(self, price, specials, needs) -> int:
        def backtrack(curr_bought, curr_cost):
            if all(curr_bought[i] >= needs[i] for i in range(len(needs))):
                self.min_cost = min(self.min_cost, curr_cost)
                return
            for special in specials:
                if any(special[i] > needs[i] - curr_bought[i] for i in range(len(needs))):  # skip deals that exceed needs
                    continue            # 这里很重要，不然会 maximum recursion depth exceeded
                next_bought = [curr_bought[i] + special[i] for i in range(len(needs))]
                backtrack(next_bought, curr_cost + special[-1])

        self.min_cost = float("inf")
        for i in range(len(price)):     # 第一步：把单买的方式也转换成specials
            special = [0 for _ in range(len(price) + 1)]
            special[i] = 1
            special[-1] = price[i]
            specials.append(special)
        backtrack([0 for _ in range(len(needs))], 0)
        return self.min_cost
        
        
        
"""
solution 2: dfs + memorization 
- O(MLN) where L is len(prices), M is how many specials are there, N is value of needs
"""
class Solution:
    def shoppingOffers(self, price, specials, needs) -> int:
        def backtrack(curr_bought):
            if all(curr_bought[i] >= needs[i] for i in range(len(needs))):
                return 0
            if tuple(curr_bought) in memo:          # check if curr_state is in memo
                return memo[tuple(curr_bought)]
            min_cost = float("inf")
            for special in specials:    # O(M)
                if any(special[i] > needs[i] - curr_bought[i] for i in range(len(needs))):  # skip deals that exceed needs
                    continue            
                next_bought = [curr_bought[i] + special[i] for i in range(len(needs))]
                min_cost = min(min_cost, backtrack(next_bought) + special[-1])
            memo[tuple(curr_bought)] = min_cost     # update memo
            return min_cost

        self.min_cost = float("inf")
        for i in range(len(price)):     # step 1: 把一个一个单买的也放进specials中
            special = [0 for _ in range(len(price) + 1)]
            special[i] = 1
            special[-1] = price[i]
            specials.append(special)
        memo = collections.defaultdict(lambda: float("inf"))  # (curr_bought --> how much more we need to spend to satisfy needs)
        return backtrack([0 for _ in range(len(needs))])
