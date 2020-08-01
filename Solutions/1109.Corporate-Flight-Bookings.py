1109. Corporate Flight Bookings

There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.

 

Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]



"""
for each interval [i, j, k], we need k more seats at day i, and we need k less seats at day j.
so we can update how many more we need on each day. - O(m+n)
"""
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        need = [0 for _ in range(n + 1)]
        for start, end, seat in bookings:
            need[start - 1] += seat
            need[end] -= seat
            
        res = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            res[i] = res[i - 1] + need[i - 1]
        return res[1:]
