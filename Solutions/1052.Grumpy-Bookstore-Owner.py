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
The first intuition is to find the larget lens in arr grumpy with at most X 0s.
Then realized we need to find the largest number of customers with at most X 0s.
Since the window size is fixed, the problem is easier to implement. We only need to update the max_gain,
which represents how man ymore people can be satisfied if the owner use X minites magic card
"""
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        lens = len(customers)
        satisfied = sum(customers[i]  * (1 - grumpy[i]) for i in range(lens))   # how many people satisfied initially
        gain = sum(customers[i] * grumpy[i] for i in range(X))  # how many more people can be satisfied if the owner use X minites magic card
        max_gain = gain
        for i in range(X, lens):
            gain += customers[i] * grumpy[i] - customers[i-X] * grumpy[i-X]
            max_gain = max(max_gain, gain)
        return max_gain + satisfied
