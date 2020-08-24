1109. Corporate Flight Bookings

There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.

 

Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]


"""
solution 1: brutal force: O(MN) TLE.
"""
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0 for _ in range(n)]
        for start, end, seats in bookings:
            for i in range(start - 1, end):
                res[i] += seats
        return res
 

"""
DP: O(m+n). for each interval [i, j, k], we need k more seats at day i, and we need k less seats at day j.
so we can pre-calculate how many more we need on each day and store in a list need.
dp[i]=how man yseats booked on day i. dp[i]=dp[i-1]+need[i]
"""
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        need = [0 for _ in range(n + 1)]    # how many more seats we need more on day i
        for start, end, seats in bookings:
            need[start - 1] += seats
            need[end] -= seats
            
        dp = [0 for _ in range(n)]  # dp[i] = how many seats booked on day i
        dp[0] = need[0]
        for i in range(1, n):
            dp[i] = dp[i-1] + need[i]
        return dp
