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
solution 1: backtrack - 
O(2^M*L*N) where L is len(prices), M is how many specials are there, N is value of needs
"""
class Solution:
    def shoppingOffers(self, prices: List[int], specials: List[List[int]], needs: List[int]) -> int:
        return self._backtrack(prices, needs, specials)
    
    def _backtrack(self, prices, curr_needs, specials):
        res = sum(p * q for p, q in zip(prices, curr_needs))     # intialize res as direct buy w/o using specials 

        # traversal the specials to find possible special that minimize the res to satisfy curr_needs
        for special in specials:
            if any(special[i] > curr_needs[i] for i in range(len(prices))):   # skip deals that exceed needs
                continue

            next_needs = []
            for i in range(len(prices)):
                next_needs.append(curr_needs[i]-special[i])
                
            res = min(res, self._backtrack(prices, next_needs, specials) + special[-1])
            
        return res
        
        
        
"""
solution 2: dfs + memorization 
- O(MLN) where L is len(prices), M is how many specials are there, N is value of needs
"""
class Solution:
    def shoppingOffers(self, prices: List[int], specials: List[List[int]], needs: List[int]) -> int:
        memo = collections.defaultdict(int)     # memo remember the minimum cost to satisfy curr_needs
        return self._backtrack(prices, tuple(needs), specials, memo)
    
    def _backtrack(self, prices, curr_needs, specials, memo):
        if curr_needs in memo:
            return memo[curr_needs]
        
        memo[curr_needs] = sum(p * q for p, q in zip(prices, curr_needs))    # intialize res as direct buy w/o using specials 

        # traversal the specials to find possible special that minimize the res to satisfy curr_needs
        for special in specials:
            if any(special[i] > curr_needs[i] for i in range(len(prices))):   # skip deals that exceed needs
                continue

            next_needs = []
            for i in range(len(prices)):
                next_needs.append(curr_needs[i]-special[i])
                
            memo[curr_needs] = min(memo[curr_needs], self._backtrack(prices, tuple(next_needs), specials, memo) + special[-1])
            
        return memo[curr_needs]
