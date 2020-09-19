"""
1011. Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 
Example 2:

Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: 
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation: 
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
"""

"""
similar with copy books
"""
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        start, end = max(weights), sum(weights) + 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._can_ship(weights, mid, D):
                end = mid
            else:
                start = mid
        return start if self._can_ship(weights, start, D) else end
    
    def _can_ship(self, weights, capacity, D):  
        """
        Return can we ship all weights with capacity within D days?
        """
        days_needed = 0
        i = 0
        while i < len(weights):
            curr_w = 0
            while i < len(weights) and curr_w + weights[i] <= capacity:
                curr_w += weights[i]
                i += 1
            days_needed += 1
        return days_needed <= D





class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        start, end = 0, sum(weights)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._can_ship(weights, mid, D):
                end = mid
            else:
                start = mid
        
        return start if self._can_ship(weights, start, D) else end
    
    def _can_ship(self, weights, capacity, D):
        cnt = 1
        added_weight = 0
        for weight in weights:
            if weight > capacity:   # if a weight > capacity, then we cannot load this weight
                return False
            
            added_weight += weight
            if added_weight > capacity:
                cnt += 1
                added_weight = weight
                
        return cnt <= D
