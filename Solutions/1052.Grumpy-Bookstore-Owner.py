"""
1052. Grumpy Bookstore Owner

Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
"""



"""
The first intuition is to find the larget lens in arr grumpy with at most X 0s.
Then realized we need to find the largest number of customers with at most X 0s.
Since the window size is fixed, the problem is easier to implement. We only need to update the max_gain,
which represents how man ymore people can be satisfied if the owner use X minites magic card
"""
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], x: int) -> int:
        satisfy = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)  # how many customer could be satisfied if not use magic x minutes.  
        max_satisfy = satisfy
        for i in range(len(customers)):
            satisfy += customers[i] if grumpy[i] == 1 else 0
            
            if i >= x:      # maintain a window with fixed size
                satisfy -= customers[i-x] if grumpy[i-x] == 1 else 0
                
            max_satisfy = max(max_satisfy, satisfy)
            
        return max_satisfy
